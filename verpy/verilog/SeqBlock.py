
from __future__ import print_function, absolute_import
from .VerilogObject import *
from .VList import AssignList
from .Assignment import NetContainer

class SeqBlock(VerilogObject):
    def __init__(self, name, kw='assign', parent=None):
        super(SeqBlock, self).__init__(name, parent)
        self.keyw = kw
        self.others = NetContainer(
                name=self.name+'otherRHS', parent=self)
        self.assigns = AssignList(parent=self)

    def copyfrom(self, frm, **kwargs):
        super(SeqBlock, self).copyfrom(frm, **kwargs)
        self.keyw = frm.keyw
        self.others = frm.other.clone()
        self.assigns = frm.assigns.clone()

    def newAssign(self, kw):
        return self.assigns.new(
                name=self.name+"asign"+str(self.parent.uninum),
                kw=kw)

    def newOtherRhs(self, kw):
        return self.others

    # this called from under assigmnent
    def referNet(self, name, arr=None):
        return self.parent.referNet(name, arr)

    def checkDriverLoad(self, nets, params=None):
        self.others.checkDriverLoad(nets, params, self)
        for i in self.assigns:
            i.checkDriverLoad(nets, params, self)

    def dump(self, indent=''):
        print("%sSequence Block: %s (%s)" % (indent, self.name, self.keyw))
        indent+='  '
        print("%sOther RHS" % indent)
        self.others.dump(indent+'  ')
        print("%sAssignments" % indent)
        for s in self.assigns:
            s.dump(indent+'  ')

