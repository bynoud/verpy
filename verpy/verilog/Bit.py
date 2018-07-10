
from __future__ import print_function, absolute_import

def _packAtLen(val, length):
    if isinstance(val, NetType):
        _d = val.pack()
    elif isinstance(val, (list, tuple)):
        _d = val
    else :
        _d = [val] * length
    # padding 0 if not full
    for i in range(len(_d), length):
        _d.append( BitGnd )
    # truncate if larger
    return _d[:length]

class NetType(object):
    DELIM = '&r;'
    BITSEP = '&b;'
    def __init__(self, name):
        self.name = name

    def addDriver(self, drvs, updateLoad=False):
        _d = _packAtLen(drvs, self.width)
        bits = self.pack()
        for i,v in enumerate(_d):
            bits[i].addDriver(v)
            if updateLoad and isinstance(v, NetType):
                v.addLoad(bits[i])

    def addLoad(self, lds, updateDriver=False):
        bits = self.pack()
        for i,v in enumerate(lds):
            if i > len(bits):
                return
            bits[i].addLoad(v)
            if updateDriver and isinstance(v, NetType):
                v.addDriver(bits[i])


    def addLoad(self, val):
        pass

    def pack(self):
        pass

    @property
    def width(self):
        pass

    def __str__(self):
        return self.name

class Bit(NetType):
    def __init__(self, name, index=-1):
        super(Bit, self).__init__(name)
        self.index = index
        self.drivers = []
        self.loads = []

    def addDriver(self, val):
        self.drivers.append(val)

    def addLoad(self, val):
        self.loads.append(val)

    def pack(self):
        return [self]

    @property
    def width(self):
        return 1

### end of Bit

BitGnd = Bit(name='__Gnd__')
BitPwr = Bit(name='__Pwr__')


class BitSlice(NetType):
    def __init__(self, name, msb=-1, lsb=-1, packed=True):
        assert (msb<0 and lsb<0) or (msb>=0 and lsb>=0)
        super(BitSlice, self).__init__(name)
        self.packed = packed
        self._msb = msb
        self._lsb = lsb
        self._bits = []
        if msb>=0:
            for i in range(msb+1):
                self._bits.append( None if i<lsb else
                        Bit(name=("%s%s%s" % (self.name, self.DELIM, i)), index=i) )

    def pack(self):
        return [x for x in self.iterBits()]

    @property
    def unkSize(self):
        return (self._msb<0)

    @property
    def msb(self):
        assert not self.unkSize
        return self._msb

    @property
    def lsb(self):
        assert not self.unkSize
        return self._lsb

    @property
    def bus(self):
        return (self.msb, self.lsb)

    @property
    def width(self):
        assert not self.unkSize
        return (self._msb - self._lsb + 1)

    def iterIndexs(self):
        if not self.unkSize:
            for i in range(self._lsb, self._msb+1):
                yield i

    def iterBits(self):
        for i in self.interIndexs():
            yield self.bits[i]

    def _bitwchk(self, m,l):
        if m > self._msb or l < self._lsb:
            raise Exception("Bit slice out-of-range [%d:%d] -> [%d:%d]" %
                            self._msb, self._lsb, m, l)

    def _slice(self, start, stop):
        assert (not self.unkSize) or start<0
        self._bitwchk(start, stop)
        if start == stop:
            bitsel = "%d" % start
        else:
            bitsel = "%d%s%d" % (start, self.BITSEP, stop)
        r = type(self)(
                name=("%s%s%s" % (self.name, self.DELIM, bitsel)),
                msb=start, lsb=stop, packed=self.packed)
        for i in range(start, stop+1):
            r._bits[i] = self._bits[i]
        return r

    def addDriver(self, drvs, updateLoad=False):
        assert not self.unkSize
        assert (not isinstance(drvs, BitSlice)) or (not drvs.unkSize)
        super(BitSlice, self).addDriver(drvs, updateLoad)

    def addLoad(self, lds, updateDriver=False):
        assert not self.unkSize
        assert (not isinstance(lds, BitSlice)) or (not lds.unkSize)
        super(BitSlice, self).addLoad(lds, updateDriver)

    def __getitem__(self, key):
        print("getitem '%s'" % key)
        if isinstance(key, slice):
            return self._slice( key.start or self._msb, key.stop or self._lsb )
        else:
            return self._bits[key]

    ## What 'a[3:2] = b' supposed to do??
    ## it should be set driver, right?
    #def __setitem__(self, key, val):
    #    r = self.__getitem__(key)
    #    r.addDriver(val)

###### end of BitSlice

class BusType(NetType):
    def __init__(self, name, dimentions=None):
        super(BusType, self).__init__(name)
        self._bus = []
        if dimentions:
            self.setDimention(dimentions)


    def setDimention(self, dims):
        def _addDim(dims, pref):
            r = []
            print("XXX %s:%s" % (pref,dims))
            if len(dims) > 0:
                m,l = dims[0]
                for i in range(m+1):
                    if i<l:
                        r.append(None)
                    else:
                        r.append(_addDim(dims[1:],
                                         "%s%s%s" % (pref, self.DELIM, i)))
            else:
                r = Bit(name=pref)
            return r
        self._bus = _addDim(dims, self.name)

    ## Verilog bit selection rule, consider 'reg [3:0][5:0] [7:0] b'
    #  c = b[2][3:1] -> this return as a object of '[2:0] [7:0]'
    #        or '[3:1] [7:0]', depend on how 'c' is declared
    #        now assume '[2:0][7:0]'
    #  then if select 'c[2] = ...' -> it point to c[2][7:0]
    #        or it b[2][3][7:]
    #  in assignment, it is:
    #       'b[2][3:1][2] = ...', selection b[2][3:1] is another object
    #       (not same as 'c' above) which is slice with [2] result in single bit

    def dump(self, indent=''):
        def _dumpbits(bits, indent=''):
            if isinstance(bits, list):
                for i in bits:
                    _dumpbits(i, indent)
            else:
                if bits is not None:
                    print("%sBit : %s" % (indent, bits.name))

        print("%sBusType : %s" % (indent,self.name))
        _dumpbits(self._bus, indent+'  ')


def flatList(mlist):
    l = []
    for i in mlist:
        if isinstance(i, (list, tuple)):
            l += flatList(i)
        else:
            l += i
    return l

class Bus(NetType):
    def __init__(self, name, dims):
        super(Bus, self).__init__(name)
        self._dims = []
        for m,l,p in dims:
            self.newDim( msb=m, lsb=l, packed=p)

    @property
    def width(self):
        w = 0
        for i in self._dims:
            w += i.width
        return w

    @property
    def ispacked(self):
        for i in self._dims:
            if not i.packed:
                return False
        return True

    def newDim(self, msb=-1, lsb=-1, packed=True):
        if packed:
            ind = len(self._dims)  # if pack, insert at the end
        else:
            ind = 0
            for i,v in enumerate(self._dims):
                if v.packed: break # find first pack array
                ind += 1
        self._dims.insert( ind, BitSlice(
            name=("%s%s%s" % (self.name, self.DELIM, len(self._dims))),
            msb=msb, lsb=lsb, packed=packed) )

    def _selectDim(self, index):
        d0 = self._dims[0]
        if index not in range(d0.lsb, d0.msb+1):
            raise Exception("Bit select out-of-range [%d:%d] <- %d" %
                    (d0.msb, d0.lsb, index))
        r = type(self)(
                name=("%s%s%d" % (self.name, self.DELIM, index)),
                dims=[]) # dont inital dimention
        for i in self._dims[1:]:
            r._dims.append(i)
        return r

    def pack(self):
        a = []
        for i in drvs._dims:
            #if not i.packed:
            #    raise Exception("cannot pack the unpacked dimention")
            for j in i.iterBits:
                a.append(j)
        return a
        

    def addDriver(self, drvs, updateLoad=False):
        if not self.ispacked:
            raise Exception("Cannot set driver for unpacked bits")
        super(Bus, self).addDriver(drvs, updateLoad)

    def addLoad(self, lds, updateDriver=False):
        if not self.ispacked:
            raise Exception("Cannot set load for unpacked bits")
        super(Bus, self).addLoad(lds, updateDriver)

    # final selection should return a BitSlice??
    def __getitem__(self, key):
        assert len(self._dims) > 0
        if len(self._dims) > 1:
            assert isinstance(key, int)
            return self._selectDim(key)
        else:
            return self._dims[0][key]

    ## This will set the driver/load
    #def __setitem__(self, key, val):
    #    r = self.__getitem__(key)
    #    r.addDriver(val)


