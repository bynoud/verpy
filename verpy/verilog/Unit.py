
from __future__ import print_function, absolute_import
from .VerilogObject import *
from .VList import ModuleList
from VerpyError import *

class Unit(VerilogObject):
    def __init__(self, options, name='$unit'):
        super(Unit, self).__init__(name=name)
        self._root = self
        self.opts = options
        self.mods = ModuleList(self)
        self.tops = ModuleList(self)

    def copyfrom(self, frm):
        super(Unit, self).copyfrom(frm)
        self.__root = self
        self.opts = frm.opts    # shallow
        self.mods = frm.mods.clone()
        self.tops = ModuleList(self) # need to run link again!!!

    def newModule(self, name, kw="module"):
        debug("new %s for %s : %s" % (kw, self.name, name))
        return self.mods.new(name=name, kw=kw)

    def link(self):
        """
        mainly use to fix hierachycal instance
        """
        self.tops = self.mods[:]
        for m in self.mods:
            for c in m.cells:
                try:
                    c.modref = self.mods[c.modname]
                    self.tops.remove(c.modname)     # not in tops, if not in mods
                except:
                    pass
        self._linked = True

    def elaborate(self, topname=''):
        # move instanced-module under thier parent
        try: self._linked
        except: self.link()
        if topname:
            if topname not in self.mods:
                raise VerpyUserError("Unknown top module name '%s'" % topname)
            self.mods[topname].elaborate()
        else:
            for m in self.tops: m.elaborate()

    def dump(self, indent=""):
        print(indent+"Unit: "+self.name)
        indent+="  "
        for m in self.tops: m.dump(indent)

    @property
    def topModules(self):
        return [ x for x in self.tops ]

