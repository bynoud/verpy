
from __future__ import print_function, absolute_import
from .VerilogObject import *
from .VList import PinList
from .ParamMixin import ParamMixin
from VerpyError import *

class Cell(VerilogObject):
    def __init__(self, name, modname="", parent=None):
        super(Cell, self).__init__(name=name, parent=parent)
        self.modname = modname
        self.modref  = None
        self.pins    = PinList(parent=self)
        self._defp   = None

    def copyfrom(self, frm, **kwargs):
        super(Cell, self).copyfrom(frm, **kwargs)
        self.modname = frm.modname
        self.modref  = None # Link must run again to correct this
        self.pins = frm.pins.clone(parent=self)
        self._defp = primaryCopy(frm._defp)

    def newPin(self, name, _dir='any'):
        return self.pins.new(name=name, direction=_dir)

    #def inferNet(self, name):
    #    return self.parent.inferNet(name)
    def referNet(self, name, arr=None):
        return self.parent.referNet(name, arr)

    # unify module-ref, by parameter value
    def _uniquify(self):
        modref = self.modref.clone()
        modref.elaborate(self._defp)
        self.modref = modref

    def _resolve_pin_connections(self):
        _pinnames = []
        debug("start to resolves : %s -> %s" % (self.name, self.pinnames))
        for (i,p) in enumerate(self.pins_order):
            try:
                p.elaborate(self.modref.ports, _pinnames)
            except VerpySyntaxError,e:
                raise VerpySyntaxError("Failed to resolve cell '%s' : %s" %
                                       self.name, e)

    def elaborate(self):
        if not self.modref: return
        self._uniquify()                # unique this instance
        self._resolve_pin_connections() # resolve pin connection

    def defparams(self,val):
        if isinstance(val,dict):
            if self._defp is None: self._defp = {}
            for (n,v) in val.items(): self._defp[n] = v
        else:
            if self._defp is None: self._defp = []
            elif isinstance(val, list):
                self._defp += val
            elif val is not None:
                self._defp.append(val)

    def checkDrivenLoad(self, nets, params=None, tbused=None):
        for p in self.pins:
            p.checkDriverLoad(nets, params, tbused)

    def dump(self, indent=""):
        print(indent+"cell: "+self.modname+" "+self.name)
        indent+="  "
        print(indent+"defparam : '%s'" % (self._defp))
        for p in self.pins: p.dump(indent)

