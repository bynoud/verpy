
from __future__ import print_function, absolute_import
from .VList import NetList
from .SliceableObject import SizeSliceable
from .AstEvaluation import eval_expression
from VerpyError import *

class Net(SizeSliceable):
    def __init__(self, name, ntype='wire', direction='net', parent=None):
        super(Net, self).__init__(name, parent)
        self.ntype = ntype
        self.direction = direction

    ## elabed net should not need to be cloneable ??
    #def copyfrom(self, frm, **kwargs):
    #    super(Net, self).copyfrom(frm, **kwargs)
    #    # simple string
    #    self.ntype = frm.ntype
    #    self.direction = frm.direction
    #    self.nets = frm.nets    # should be shallow??
    #    # array-of-array
    #    self._rawbus = primaryCopy(frm._rawbus)
    #    self._rawref = primaryCopy(frm._rawref)

    def dump(self, indent=""):
        #print(indent+self.direction+": "+str(self.ntype)+" ", end="")
        print("%s%s: %s %s" % (indent, self.direction, self.ntype, self.decl))
        indent+='  '
        if self._rawbus:
            print("%srawbus %s" % (indent, self._rawbus))
        if self._rawref:
            print("%srefbus %s" % (indent, self._rawref))
        #print("%sDrivers : " % indent)
        self.dumpDrivers(indent)
        #print("%sLoads : " % indent)
        self.dumpLoads(indent)
        if self.undrivens:
            print("%sUNDRIVENS :" % indent, end='')
            for u in self.undrivens: print(" %s," % u, end='')
            print("")
        if self.unloads:
            print("%sUNLOADS:" % indent, end='')
            for u in self.unloads: print(" %s," % u, end='')
            print("")


class Port(Net):
    pass

class Parameter(Net):
    def __init__(self, name, ntype):
        super(Parameter, self).__init__(name=name, ntype=ntype, direction='net')
        self.val = ''

    #def copyfrom(self, frm, **kwargs):
    #    super(Parameter, self).copyfrom(frm, **kwargs)
    #    self.val = frm.val

    def dump(self, indent=""):
        print("%s%s: %s = %s" % (indent, self.ntype, self.name, self.val))


### pre-elabed version
from .VerilogMixin import PrimCloneableMixin

class ANet(PrimCloneableMixin):
    def __init__(self, name, ntype='wire', direction='net'):
        self.name = name
        self.ntype = ntype
        self.direction = direction
        self._rawbus = []   # decl bus
        self._refbus = []   # array-of-array reference
        self._bus = []

    # re-declare is possible (for ANSI style)
    # at pre-elab, some time cannot check bitwidth to make sure they are same
    def declBus(self, parr, uarr):
        if uarr is None: uarr = []
        self._rawbus.append( [ [x[0],x[1],False] for x in uarr ] +
                             [ [x[0],x[1],True]  for x in parr ] )

    def refBus(self, arr):
        self._refbus.append(arr)

    def _buswidthResolve(self, params=None):
        if not self._rawbus: return
        # resolve buswidth first
        for (i,a) in enumerate(self._rawbus):
            if len(a) != len(self._bus):
                raise VerpySyntaxError("Decl bus size mismatch")
            for (j,a2) in enumerate(a):
                a[j] = [eval_expression(a2[0], params),
                       eval_expression(a2[1], params), a2[2]]
            # check for consistency
            if i==0:
                self._bus = a
            elif self._bus != a:
                raise VerpySyntaxError("Decl bus width mismathc")
        self._rawbus = []

    # reference check
    def _busrefCheck(self, params):
        if not self._rawref: return
        for (i,a) in enumerate(self._rawref):
            if len(a) > len(self._bus):
                raise VerpySyntaxError("Reference out-of-index")
            for (j,a2) in enumerate(a):
                m,l = (eval_expression(a2[0], params),
                       eval_expression(a2[1], params))
                if m>self._bus[j][0] or l<self._bus[j][1]:
                    raise VerpySyntaxError("Reference out-of-bit range")
        self._rawref = []

    # return a real Net object
    def elaborate(self, parent, params=None):
        try:
            self._buswidthResolve(params)
            self._busrefCheck(params)
            n = Net(self.name, self.ntype, self.direction, parent)
            for d in self._bus:
                n.new_dim(*d)
            n.init_driverload()
            return n
        except VerpySyntaxError, e:
            raise VerpyElabError("elab failed, net '%s' : %s" % (self, e))

