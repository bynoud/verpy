
from __future__ import print_function, absolute_import
from .VerilogMixins import CloneableMixin
from .VerilogObject import VerilogObject
from VerpyError import *
from collections import MutableSequence
from types import StringTypes

class VList(MutableSequence, CloneableMixin):
    def __init__(self, parent, clstype=VerilogObject):
        assert issubclass(clstype, VerilogObject)
        self._parent = parent
        self._cls = clstype
        self._items = []
        self._names = {}

    def copyfrom(self, frm, **kwargs):
        if 'parent' in kwargs:
            print("VList copyfrom parent applied %s" % type(self))
            self.parent = kwargs['parent']
        else:
            self.parent = frm._parent
        self._cls = frm._cls
        self._items = []
        self._names = {}
        for v in frm._items:
            self.insert(v.clone(**kwargs))

    def new(self, clstype=None, **kwargs):
        if clstype is None: clstype = self._cls
        assert 'name' in kwargs
        assert issubclass(clstype, self._cls)
        return self.insert(clstype(**kwargs))

    def insert(self, item, ind=-1):
        assert isinstance(item, self._cls)
        name = item.name
        assert name not in self._names
        if item.parent is None:
            item.parent = self.parent

        if ind<0:
            item.index = len(self)
            self._items.append(item)
        else:
            item.index = ind
            self._items.insert(item, ind)
        self._names[name] = item.index
        return item

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, val):
        self._parent = val
        for x in self._items: x.parent = val

    def _itemoper(self, op, key, *args):
        from types import StringTypes
        if isinstance(key, (int, StringTypes)):
            return getattr(self, op)(key, *args)
        elif isinstance(key, slice):
            return getattr(self, op+'s')(key.start or 0, key.stop or len(self), *args)
        elif isinstance(key, tuple):
            return getattr(self, op+'s')(key, *args)

    ## abtract method need to override
    def __getitem__(self, key):
        return self._itemoper('getItem', key)

    def __setitem__(self, key, val):
        assert isinstance(key, self._cls)
        self._itemoper('setItem', key, val)

    def __delitem__(self, key):
        self._itemoper('delItem', key)

    def __len__(self):
        return len(self._items)

    # i in o -> __contains__(o,i)
    def __contains__(self, item):
        if isinstance(item, StringTypes):
            return (item in self._names)
        else:
            return (item in self._items)

    def getAttrs(self, name):
        return [getattr(x, name) for x in self._items]

    def setAttrs(self, name, val):
        vals = val
        if not isinstance(val, list):
            vals = [val] * len(self)
        for (i,v) in enumerate(self._items):
            setattr(v, name, vals[i])

    def getItem(self, ind):
        if isinstance(ind, StringTypes):
            ind = self._names[ind]
        return self._items[ind]

    def getItems(self, start, stop):
        return self.filter(lambda x: start <= x.index < stop)

    def setItem(self, ind, val):
        if isinstance(ind, int):
            ind = self._names[ind]
        self._items[ind] = val

    def setItems(self, start, stop, vals):
        for i in range(start, stop):
            self._items[i] = vals[i]

    def delItem(self, ind):
        name = ind
        if isinstance(ind, int):
            name = self._items[ind].name
        else:
            ind = self._names[ind]
        del self._items[ind]
        del self._names[name]

    def delItems(self, start, stop):
        for i in range(start, stop):
            del self._names[self._items[i].name]
        del self._items[start, stop]

    def filter(self, func):
        if func is None:
            func = lambda x: x is not None
        c = type(self)(parent=self._parent)
        for v in self._items:
            if func(v): c.insert(v)
        return c

    def keys(self):
        return [x.name for x in self._items]
    def iterkeys(self):
        for x in self._items: yield x.name

    def values(self):
        return x._items
    def itervalues(self):
        for x in x._items: yield x

    def items(self):
        return [(x.name, x) for x in self._items]
    def iteritems(self):
        for x in self._items: yield x.name, x

class ModuleList(VList):
    def __init__(self, parent):
        from .Module import Module
        super(ModuleList,self).__init__(parent, Module)

class CellList(VList):
    def __init__(self, parent):
        from .Cell import Cell
        super(CellList,self).__init__(parent, Cell)

class PinList(VList):
    def __init__(self, parent):
        from .Pin import Pin
        super(PinList,self).__init__(parent, Pin)

class NetList(VList):
    def __init__(self, parent):
        from .Net import Net
        super(NetList,self).__init__(parent, Net)

class AssignList(VList):
    def __init__(self, parent):
        from .Assignment import Assignment
        super(AssignList,self).__init__(parent, Assignment)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__assign_' + str(self.parent.uninum) + '__'
        return super(AssignList, self).new(clstype, **kwargs)

class ContainerList(VList):
    def __init__(self, parent):
        from .Assignment import NetContainer
        super(ContainerList,self).__init__(parent, NetContainer)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__container_' + str(self.parent.uninum) + '__'
        return super(ContainerList, self).new(clstype, **kwargs)

class SeqblkList(VList):
    def __init__(self, parent):
        from .SeqBlock import SeqBlock
        super(SeqblkList,self).__init__(parent, SeqBlock)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__Seqblk_' + str(self.parent.uninum) + '__'
        return super(SeqblkList, self).new(clstype, **kwargs)

