
from __future__ import print_function

import sys
sys.path.insert(0,'/user/ductt/python/antlr4-master/runtime/Python2/src')
from antlr4 import *
from VerexHelper import *
from Netlist import Netlist

class ListenerContainer(object):
    def __init__(self, cont, ctx):
        self.cont = cont
        self.ctx = ctx

    def isSelf(self, ctx): return (self.ctx == ctx)

class IOListener(ParseTreeListener):
    def __init__(self, parser):
        self._parser = parser
        self._tokens = parser.getTokenStream()
        self._netlist = parser._netlist
        self._actMod  = None
        self.cont = self._netlist
        self.contStack = []

    def pushCont(self, cont, ctx):
        self.contStack.append(ListenerContainer(self.cont, ctx))
        self.cont.addContainer(cont)
        self.cont = cont

    def popCont(self, ctx):
        if self.contStack and self.contStack[-1].isSelf(ctx):
            self.cont = self.contStack.pop().cont

    # global tasks
    def exitEveryRule(self, ctx): self.popCont(ctx)

    def visitTerminal(self, node):
        txt = node.getText()
        if self.cont is not None:
            self.cont.addContext(node)
            ## take hidden channel
            hidtoks = self._tokens.getHiddenTokensToRight(node.getSymbol().tokenIndex)
            if hidtoks is not None:
                for hid in hidtoks: self.cont.addText(hid.text)

    def enterModule_declaration(self, ctx):
        debug("enter Module decl : %s" % (type(ctx)))
        m = self.cont.newModule(
                ctx.module_identifier().getText(),
                ctx.module_keyword().getText()
                );
        self._actMod = m
        self.pushCont(m, ctx)

    def enterParameter_declaration_(self, ctx):
        # just ignore the 'range_'
        for c in ctx.list_of_param_assignments().param_assignment():
            self.cont.parameters = [
                    c.parameter_identifier().getText(),
                    c.constant_expression().getText()]

    def enterLocal_parameter_declaration(self, ctx):
        # just ignore the 'range_'
        for c in ctx.list_of_param_assignments().param_assignment():
            self.cont.localparams = [
                    c.parameter_identifier().getText(),
                    c.constant_expression().getText()]

    # port header inside module <name> (portname [...] , portname, [...])
    def enterPort_reference(self, ctx):
        p = self.cont.newPortHeader(
                ctx.port_identifier().getText())
        if ctx.constant_expression():
            p.rawBusarr(ctx.constant_expression().getText())
        elif ctx.range_expression():
            p.rawBusarr(rexpr2arr(ctx.range_expression()))


    # port declare inside module <name> ( input ..., out ...)
    # or declare after module <name (...); input ...
    def enterPort_declaration(self, ctx):
        dir_ = ctx.portkw.text
        ntype = 'wire'
        if ctx.net_type() != None : ntype = ctx.net_type().getText()
        elif ctx.regtype != None  : ntype = ctx.regtype.text

        parr = range2arr(ctx.range_())
        for pctx in ctx.list_of_port_identifiers().port_identifier():
            p = self.cont.newPort( pctx.getText(), dir_, ntype)
            p.rawBusarr(parr)

    def enterNet_declaration(self, ctx):
        ntype = ctx.net_type().getText() \
                if ctx.net_type() != None else ctx.regtype.text
        parr = range2arr(ctx.range_())
        if ctx.list_of_net_identifiers() != None:
            for nctx in ctx.list_of_net_identifiers().net_identifier_wrange():
                inferNetFromDecl(self.cont, nctx, ntype, parr)
        else:
            for nctx in ctx.list_of_net_decl_assignments().net_decl_assignment():
                inferNetFromDecl(self.cont, nctx, ntype, parr)
                inferNetsFromExpr(self.cont, nctx.expression())

    # reg decl
    def enterReg_declaration(self, ctx):
        parr = range2arr(ctx.range_())
        for nctx in ctx.list_of_variable_identifiers().variable_type():
            # dont support constant assignment
            inferNetFromDecl(self.cont, nctx, 'reg', parr)


