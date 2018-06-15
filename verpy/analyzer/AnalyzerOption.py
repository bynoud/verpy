
from __future__ import print_function, absolute_import
import os.path
from VerpyError import *

def _uniapp(tol, val):
    if val not in tol:
        tol.append(val)

def _filebase(name):
    return os.path.splitext(os.path.basename(name))[0]

def _fname(name, relpath=''):
    if relpath:
        relpath += '/'
    return os.path.abspath(relpath+name)

class AnalyzerOption(object):
    def __init__(self, fromstr=''):
        self.files = []
        self.defines = {}
        self.incdirs = []
        self.liddirs = []
        self.libfiles = {}
        self.libexts = ['.v']    # default '.v' for libext
        if fromstr:
            self.strOpt(fromstr)

    # Support VCS like options:
    # +define+DEFINE=VAL+OTHER
    # +incdir+/file/name
    # +libext+.v
    # -y /folder/name
    # -v /file/name
    # -f /file/name -F /file/name
    # /file/name
    def strOpt(self, fstr, relpath=''):
        opts = fstr.split()
        i = 0
        while i < len(opts):
            if opts[i] == '-v':
                i += 1
                _uniapp(self.libfiles, _fname(opts[i], relpath))
            elif opts[i] == '-y':
                i += 1
                _uniapp(self.libdirs, _fname(opts[i], relpath))
            elif opts[i] in ('-f', '-F'):
                self.parseFileList(opts[i+1], opts[i] == '-F')
                i+=1
            elif opts[i][0] == '+':
                vs = opts[i][1:].split('+')
                if vs[0] == 'define':
                    for d in vs[1:]:
                        k,v = (d.split('=') + [''])[:2]
                        self.newDefine(k, v)
                elif vs[0] == 'incdir':
                    for d in vs[1:]:
                        _uniapp(self.incdirs, d)
                elif vs[0] == 'libext':
                    for d in vs[1].split(','):
                        _uniapp(self.libexts, d)
                else:
                    raise VerpyLibraryError("Unknown options '%s'" % opts[i])
            else:
                self.newFile(_fname(opts[i], relpath))
            i += 1

    def parseFileList(self, fname, rel=False):
        relpath =  _fname(os.path.dirname(fname)) if rel else ''
        with open(fname) as fh:
            flines = fh.readlines()
        import re
        opts = ''
        for l in flines:
            l = l.strip(); l = re.sub(r'//.*$', '', l)
            opts += l
        self.strOpt(opts, relpath)

    def newDefine(self, name, val=''):
        r = self.defines[name] = self.UserDefine(name)
        r.body = val
        return r

    def delDefine(self, name):
        name = name.strip()
        if name in self.defines:
            del self.defines[name]

    def resetDefine(self):
        self.defines = {}

    def expandDefines(self, name, *args):
        return self.defines[name].expand(*args)

    def findIncludeFile(self, name):
        for d in self.incdirs:
            if os.path.isfile(d+'/'+name):
                return _fname(d+'/'+name)
        raise VerpyLibraryError("Included file '%s' not found" % name)

    def newFile(self, name):
        if name not in self.files:
            self.files.append(self.VerilogFile(name))

    def findLibFile(self, name):
        names = [(name + x) for x in self.libexts]
        for f in self.libfiles:
            if os.path.basename(f) in names:
                return f
        for d in self.libdirs:
            for f in names:
                if os.path.isfile(d+'/'+f):
                    return _fname(d+'/'+f)
        raise VerpyLibraryError("lib for '%s' not found" % name)

    def unprocessedFiles(self):
        return [x.fullname for x in self.files if not x.parsed]

    class UserDefine(object):
        def __init__(self, name):
            self.name = name
            self.args = []
            self._body = ''

        def addArg(self, arg):
            self.args.append(arg)

        @property
        def body(self):
            return self._body

        # must be set after all Argunments set
        @body.setter
        def body(self, val):
            txt = val.replace("\\\n", "\n")
            import re
            for a in self.args:
                txt = re.sub(r'\b'+a+r'\b', '{'+a+'}', txt)
            self._body = txt

        def expand(self, *args):
            if len(self.args) != len(args):
                raise VerpySyntaxError("Wrong argument for macro '%s'" % self.name)
            d = {}
            for i,v in enumerate(args):
                d[ self.args[i] ] = args[i]
            return self._body.format(**d)

    class VerilogFile(object):
        def __init__(self, name):
            self.fullname = os.path.abspath(name)
            self.basename = os.path.basename(name)
            self.filebase = os.path.splitext(self.basename)[0]
            self.parsed = False
            self.modules = []   # list of module in this file


