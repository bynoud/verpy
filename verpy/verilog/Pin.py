
from __future__ import print_function, absolute_import
from .VerilogObject import *
from .VerilogMixins import ContainableMixin
from .Net import *
from VerpyError import *

class Pin(Net, ContainableMixin):
    def __init__(self, name, direction='any', parent=None):
        super(Pin, self).__init__(name, 'pin', direction, parent)
        self.port = None            # port reference

    #def copyfrom(self, frm, **kwargs):
    #    super(Pin, self).copyfrom(frm, **kwargs)
    #    self.port = frm.port
    #    self.containerCopy(frm, **kwargs) 

    def setPortRef(self, port):
        if self.direction != 'any' and self.direction != port.direction:
            raise VerpySyntaxError("Port direction '%s' different from pin '%s'" %
                    self.direction, port.direction)
        self.port = port
        self.direction = port.direction
        for a in port._arr: self.new_dim(*a)

    def elaborate(self, ports, elabed):
        name = self.name
        if name not in ports.names:
            raise VerpySyntaxError("Port '%s' not found" % self.name)
        self.setPortRef(ports[name])
        elabed.append(name)

    def checkDriverLoad(self, nets, params=None, tbused=None):
        # for net driven
        tbused = tbused or self
        self.containerResolve(nets, params)
        for n in self.containerIter():
            if self.direction in ('out', 'inout'):
                n.setDrivers(tbused)
            if self.direction in ('in', 'inout'):
                n.setLoads(tbused)
        #self.containerDel()

    def dump(self, indent):
        super(Pin, self).dump(indent)
        indent+='  '
        self.containerDump(indent)


### end of Pin

class APin(ANet):
    def __init__(self, name, direction='any'):
        super(APin, self).__init__(name=name, ntype='pin', direction=direction)
        ContainableMixin.init(self) # list on nets connect to pin

    # params is of Module which contain the Cell
    def elaborate(self, ports, elabed, params):
        name = self.name
        if name not in ports.names:
            raise VerpySyntaxError("Port '%s' not found" % self.name)
        self.setPortRef(ports[name])
        elabed.append(name)

