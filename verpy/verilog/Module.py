
from __future__ import print_function, absolute_import
from .VerilogObject import *
from .ParamMixin import ParamMixin
from .VList import *
from VerpyError import *

class Module(VerilogObject, ParamMixin):
    def __init__(self, name='', kw='module', parent=None):
        super(Module, self).__init__(name, parent)
        self.keyw  = kw
        self._nets  = NetList(parent=self)
        self.cells = CellList(parent=self)
        self.assigns = AssignList(parent=self)
        self.seqs    = SeqblkList(parent=self)
        self.paramInit(self._nets)

    # deepcopy
    def copyfrom(self, frm, **kwargs):
        super(Module, self).copyfrom(frm, **kwargs)
        self.keyw = frm.keyw
        self._nets = frm._nets.clone(parent=self)
        self.cells = frm.cells.clone(parent=self)
        self.assigns = frm.assigns.clone(parent=self)
        self.seqs = frm.seqs.clone(parent=self)

    def newCell(self, instname, modname):
        debug("newcell '%s' :  %s <- %s" % (self.name, instname, modname))
        return self.cells.new(name=instname, modname=modname)

    def newPortHeader(self, name):
        return self.newNet(name, 'wire', 'header')

    def newPort(self, name, direction, ntype='wire'):
        return self.newNet(name, ntype, direction)

    def newNet(self, name, ntype='wire', direction='net'):
        debug("newnet '%s' :  %s %s %s" %
                (self.name, direction, ntype, name))
        if name in self._nets.keys():
            p = self._nets[name]
            # can only redefine if it header or port
            if p.direction == direction:
                raise VerpySyntaxError("redefined %s '%s" % (direction, name))
            # cannot redefine net
            elif p.direction not in ('input', 'output', 'port', 'header'):
                raise VerpySyntaxError("net type is illegal changed")
            # only 'header' type will be changed
            if p.direction == 'header': p.direction = direction
            p.ntype = ntype
        else:
            debug('module %s new net %s' % (self.name, name))
            p = self._nets.new(name=name, ntype=ntype, direction=direction)
        return p

    def referNet(self, name, arr=None):
        if name not in self._nets:
            #p = self._nets.new(name=name, ntype='wire', direction='infer')
            raise VerpySyntaxError("Net '%s' not found in module '%s'" %
                    (name, self.name))
        debug('module %s refer net %s' % (self.name, name))
        p = self._nets[name]
        if arr is not None:
            p.refBus(arr)
        return p

    def delNet(self, name):
        self._nets.remove(name)

    def newAssign(self, kw):
        debug('module %s new assign %s' % (self.name, kw))
        return self.assigns.new(kw=kw)
    
    def newSeq(self, kw):
        debug('module %s new seq %s' % (self.name, kw))
        return self.seqs.new(kw=kw)

    def elaborate(self, defparams=None):
        # resolve parameter first
        ParamMixin.elaborate(self, defparams)
        for n in self.nets: n.elaborate(self.parameters)
        for c in self.cells: c.elaborate()
        for a in self.assigns: a.elaborate()
        for c in self.seqs: c.elaborate()
        # check for driver/load
        for c in self.cells:    c.checkDriverLoad(self._nets, self.parameters)
        for a in self.assigns:  a.checkDriverLoad(self._nets, self.parameters)
        for c in self.seqs:     c.checkDriverLoad(self._nets, self.parameters)
        self.checkDriverLoad()

    def checkDriverLoad(self, tbused=None):
        for p in self.ports:
            if p.direction in ('input', 'inout'):
                p.setDrivers(tbused or "<%s>" % p.direction)
            if p.direction in ('output', 'inout'):
                p.setLoads(tbused or "<%s>" % p.direction)


    @property
    def nets(self):
        from .ParamMixin import _isParam
        return self._nets.filter(lambda x: not _isParam(x))

    def _getPorts(self, dir_=None):
        from types import StringTypes
        if dir_ is None:
            dir_ = ('header', 'input', 'output', 'inout', 'port')
        elif isinstance(dir_, StringTypes):
            dir_ = (dir_)
        return self._nets.filter(lambda x: x.direction in dir_)

    @property
    def ports(self): return self._getPorts()
    @property
    def inputs(self): return self._getPorts('input')
    @property
    def outputs(self): return self._getPorts('output')
    @property
    def inouts(self): return self._getPorts('inout')
    @property
    def unknownPorts(self): return self._getPorts('port')
    @property
    def headerPorts(self): return self._getPorts('header')

    def dump(self, indent=""):
        print(indent+"Module: "+self.name)
        indent+="  "
        for k in self.parameters.iterkeys():
            self._nets[k].dump(indent)
        for n in self.nets: n.dump(indent)
        for c in self.cells: c.dump(indent)
        for a in self.assigns: a.dump(indent)
        for c in self.seqs: c.dump(indent)


