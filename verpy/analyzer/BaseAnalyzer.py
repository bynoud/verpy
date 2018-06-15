
from __future__ import print_function, absolute_import

import logging
from antlr4 import *
from verilog.Unit import Unit
from VerpyError import *
from .AnalyzerOption import AnalyzerOption

logger = logging.getLogger(__name__)
def debug(msg, *args): logger.debug(msg, *args)
def info(msg, *args): logger.info(msg, *args)
def warning(msg, *args): logger.warning(msg, *args)


def range2arr(ctx):
    ret = []
    if ctx != None:
        if ctx.msb != None :
            ret.append( [ctx.msb.getText(), ctx.lsb.getText()] )
        else :
            ret.append( [ctx.star.text] )
    return ret

def rexpr2arr(ctx):
    if ctx is None: return []
    if ctx.expression():
        return [ctx.expression().getText()]*2
    if ctx.msb_constant_expression():
        return [ctx.msb_constant_expression().getText(),
                ctx.lsb_constant_expression().getText()]
    if ctx.base_expression():
        b = ctx.base_expression().getText()
        if ctx.inckey:
            return [   b+'-1+'+ctx.width_constant_expression().getText(), b]
        else:
            return [b, b+'+1-'+ctx.width_constant_expression().getText()]
    else:
        return [ctx.star.text]*2

def dim2arr(ctx):
    ret = []
    if ctx != None:
        for d in ctx:
            if d.bit != None   :
                ret.append(d.bit.getText())
            elif d.msb != None :
                ret.append( [d.msb.getText(), d.lsb.getText()] )
            else :
                ret.append([ctx.star.text])
    return ret

_contStack = []
def initCont():
    #_contStack = []
    while len(_contStack) > 0: _contStack.pop()
def pushCont(cont):
    debug("%sPush %s" % ("  "*len(_contStack), type(cont)))
    _contStack.append(cont)
    return cont
def popCont():
    debug("%sPop %s" % ("  "*(len(_contStack)-1), type(curCont())))
    try: return _contStack.pop()
    except: raise InternalFatal("contStack overflow")
def curCont():
    try: return _contStack[-1]
    except: return None

def initDefaultChild(s):
    import re
    nodes = {}
    for c in s.split():
        #if c[0] in ('>', '!', '?', '-'): continue
        if c[:2] == '>>':
            visit = 'visit' + c[2].upper() + c[3:]
            nodes[visit] = 'visitChildren' # all grand
        elif re.match(r'[a-z_]', c):
            visit = 'visit' + c[0].upper() + c[1:]
            nodes[visit] = 'visitChilds'    # only childs
    return nodes

class BaseAnalyzer(ParseTreeVisitor):
    def __init__(self, vunit=None, options=None):
        initCont()
        self._savedctx = {}
        self._visitChildNodes = {}
        self.opts = options or AnalyzerOption()
        if not vunit:
            vunit = Unit(options=self.opts)
        pushCont(vunit)

    # default visit will go through all children & grand-child ...
    # we only want to go to children
    def visitChildren(self, node):
        debug("visitChildren %s" % type(node))
        super(BaseAnalyzer, self).visitChildren(node)

    def visitChilds(self, node):
        #self.visitChildren(node, False)
        n = node.getChildCount()
        debug("visitChilds %s : %d" % (type(node), n))
        for i in range(n):
            c = node.getChild(i)
            visit = 'visit' + type(c).__name__[:-7]
            try:
                proc = getattr(self, visit)
            except AttributeError, e:
                try:
                    proc = getattr(self, self._visitChildNodes[visit])
                except KeyError, e:
                    proc = None
            if proc is not None:
                proc(c)

    def visitErrorNode(self, node):
        raise VerpySyntaxError("Parser failed: %s" % node)

    from parser import VerexParser, VerexLexer
    from .PreprocLexer import PreprocLexer
    @classmethod
    def _parse(cls, vunit=None, filename='', fromstr='',
              srcName='', entry=None, analyzerInitOpt={},
              ParserClass=VerexParser, parserInitOpt={},
              LexerClass=PreprocLexer, lexerInitOpt={},
              options=None, optstr=''):
        from .PRCHelper import createInputStream
        if filename:
            info("Analyzing file '%s' ..." % filename)
        else:
            info("Analyzing String for Rule '%s' ..." % entry)
        istr = createInputStream(filename=filename,
                                 fromstr=fromstr, srcName=srcName)

        if options is None:
            if vunit is not None:
                options = vunit.getRoot().opts
            else:
                options = AnalyzerOption(optstr)
        lexerInitOpt['options'] = analyzerInitOpt['options'] = options

        parser = ParserClass(
            CommonTokenStream(
                LexerClass(istr, **lexerInitOpt),
            ), **parserInitOpt )
        parser.buildParseTrees = True
        
        if not entry:
            tree = parser.vfile()
        else:
            try:
                tree = getattr(parser,entry)()
            except AttributeError:
                raise VerpyUserError("Parser %s doesnt have entry '%s'" %
                                     (type(parser), entry))
                
        visitor = cls(vunit, **analyzerInitOpt)
        visitor.visitChilds(tree)   # dont use visit or accept, it visit Grand
        # safe gaurd
        if len(_contStack) != 1:
            raise InternalFatal("Analyzing failed")
        return curCont()

    # parse a file or list of file
    @classmethod
    def parse(cls, srcList, vunit=None, options=None):
        assert isinstance(srcList, (list, tuple))
        if options is None:
            options = AnalyzerOption()
        options.strOpt(' '.join(srcList))
        for f in options.unprocessedFiles():
            vunit = cls._parse(vunit=vunit, filename=f, options=options) 
        return vunit

    # to parser string, you need create Unit and Module in advance
    @classmethod
    def parseString(cls, srcStr, vunit, entry=None):
        return cls._parse(fromstr=srcStr, vunit=vunit, entry=entry)

