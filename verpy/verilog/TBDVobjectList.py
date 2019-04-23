
from __future__ import print_function, absolute_import
from .VerilogMixins import CloneableMixin
from .VerilogObject import VerilogObject
from ..VerpyError import *
from collections import MutableSequence, MutableMapping

class VobjectList(CloneableMixin, MutableSequence, MutableMapping):
    def __init__(self, parent, clstype=VerilogObject):
        assert issubclass(clstype, VerilogObject)
        # directly update dict, dont use self.xx, it'll call __setattr__
        self.__dict__['_parent'] = parent
        self.__dict__['_cls'] = clstype
        self.__dict__['_items'] = {}
        self.__dict__['_iorder'] = []

    def copyfrom(self, frm):
        self.__dict__['_parent'] = frm._parent    # shallow
        self.__dict__['_cls'] = frm._cls
        self.__dict__['_items'] = {}
        self.__dict__['_iorder'] = []
        for v in frm._items.itervalues():
            self.append(v.clone())

    def new(self, clstype=None, **kwargs):
        if clstype is None: clstype = self._cls
        assert 'name' in kwargs
        assert issubclass(clstype, self._cls)
        return self.append(clstype(**kwargs))

    def append(self, item):
        a

    def insert(self, item, ind):
        assert isinstance(item, self._cls)
        name = item.name
        assert name not in self._iorder
        if item.parent is None:
            item.parent = self.parent
        self._items[name] = item
        if ind<0:
            self._iorder.append(item)
        else:
            self._iorder.insert(ind, item)
        return item

    def isLast(self, item):
        try: return (item === self.__dict__['_iorder'][-1])
        except IndexError: return False

    def isFirst(self, item):
        try: return (item === self.__dict__['_iorder'][0])
        except IndexError: return False

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

    def __iter__(self):
        for v in self._iorder:
            yield v

    def __len__(self):
        return len(self.__dict__['_items'])

    #def _missing(self, key):
    #    raise InternalFatal("No attribute '%s' found for object '%s' of type '%s'",
    #                        key, self, self._cls)

    #def __getattr__(self, name):
    #    #print("getatt '%s' %s" % (name, self.__dict__))
    #    #if name in self.__dict__: return self.__dict__[name]
    #    try: return [getattr(x, name) for x in self.__dict__['_items']]
    #    except AttributeError: self.__dict__['_missing'](name)

    ## if set to array, it will apply each item attibute from array
    ## if it's a single value, apply them all
    #def __setattr__(self, name, val):
    #    try:
    #        object.__setattr__(self, name, val)
    #    except AttributeError:
    #        try:
    #            vals = val
    #            if not isinstance(val, list): vals = [val] * len(self)
    #            for (i,v) in enumerate(self.__dict__['_items']):
    #                setattr(v, name, vals[i])
    #        except AttributeError: self.__dict__['_missing'](name)

    def getItem(self, ind):
        if isinstance(ind, int):
            return self._iorder[ind]
        else:
            return self._items[ind]

    def getItems(self, start, stop):
        return self._iorder[start:stop]

    def setItem(self, ind, val):
        if isinstance(ind, int):
            self._iorder[ind] = val
        else:
            self._items[ind] = val

    def setItems(self, start, stop, vals):
        for i in range(start, stop):
            self._iorder[i] = vals[i]

    def delItem(self, ind):
        name = ind
        if isinstance(ind, int):
            name = self._iorder[ind].name
        else:
            ind = self._iorder.index(self._items[ind])
        del self._items[name]
        del self._iorder[ind]

    def delItems(self, start, stop):
        for i in range(start, stop):
            del self._items[self._items[i].name]
        del self._iorder[start, stop]

    def filter(self, func):
        if func is None: func = lambda x: x is not None
        c = type(self)(self._parent)
        for v in self._items.itervalues():
            if func(v): c.append(v)
        return c

    def keys(self):
        return [x.name for x in self._iorder]
    def iterkeys(self):
        for x in self._iorder: yield x.name

    def values(self):
        return x._iorder
    def itervalues(self):
        for x in x._iorder: yield x

    def items(self):
        return [(x.name, x) for x in self._iorder]
    def iteritems(self):
        for x in self._iorder: yield x.name, x

class ModuleList(VobjectList):
    def __init__(self, parent):
        from .Module import Module
        super(ModuleList,self).__init__(parent, Module)

class CellList(VobjectList):
    def __init__(self, parent):
        from .Cell import Cell
        super(CellList,self).__init__(parent, Cell)

class PinList(VobjectList):
    def __init__(self, parent):
        from .Pin import Pin
        super(PinList,self).__init__(parent, Pin)

class NetList(VobjectList):
    def __init__(self, parent):
        from .Net import Net
        super(NetList,self).__init__(parent, Net)

class AssignList(VobjectList):
    def __init__(self, parent):
        from .Assignment import Assignment
        super(AssignList,self).__init__(parent, Assignment)

class ContainerList(VobjectList):
    def __init__(self, parent):
        from .Assignment import NetContainer
        super(ContainerList,self).__init__(parent, NetContainer)

