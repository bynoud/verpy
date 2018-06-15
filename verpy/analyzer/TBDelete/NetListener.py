
from __future__ import print_function

import sys
sys.path.insert(0,'/user/ductt/python/antlr4-master/runtime/Python2/src')
from antlr4 import *
from IOListener import IOListener
from VerexHelper import *

class NetListener(IOListener):
    def __init__(self, parser):
        super(NetListener, self).__init__(parser)
        self._insideProc = False


    # assignment
    def _enterNetAssignment(self, ctx):
        lhs = inferNetsFromLhs(self.cont, ctx)
        debug("LHS net lists: %s" % lhs)
        if len(lhs)>0:
            for i in lhs:
                if i.isPatt:
                    self.pushCont(i, ctx) # only first pattern i
                    debug("Found pattern on LHS: %s" % i.name)
                    break
        inferNetsFromExpr(self.cont, ctx.expression())

    def enterNet_assignment(self, ctx):
        self._enterNetAssignment(ctx)

    # cell instance/parameter override
    def enterModule_instantiation(self, ctx):
        modname = ctx.module_identifier().getText()
        defparams = getDefParameterAssignment(ctx.parameter_value_assignment())
        for minst in ctx.module_instance():
            c = self.cont.newCell(
                    minst.name_of_instance().getText(),
                    modname)
            c.defparams = defparams

    def enterModule_instance(self, ctx):
        self.pushCont( self.cont.cells[
                ctx.name_of_instance().getText()], ctx )

    def enterSpecial_port_connection(self,ctx):
        pass

    # TODO : dont infer ordered port connection for now
    def enterMixed_port_connection(self, ctx):
        p = self.cont.newPin(ctx.port_identifier().getText())
        if ctx.PinDirection() != None:
            d = ctx.PinDirection().getText()[1:] # remove first '$'
            if d != 'any' and ('put' not in d): d += 'put'
            p.direction = d
        self.pushCont(p, ctx)   # allow normal pin connection have replacement as *
        #pexpr = ctx.port_connection_expression()
        #if pexpr is None:
        #    pass
        #elif pexpr.expression() != None:
        #    p.setConn(pexpr.expression().getText(),
        #            self.inferNetsFromExpr(pexpr.expression()))
        #else: # simgle '*'
        #    p.addRepl('r/$1/')

    def enterPort_connection_expression(self, ctx):
        inferNetsFromExpr(self.cont, ctx.expression())

    ## proceduce block
    def enterInitial_construct(self, ctx): self._insideProc = True
    def exitInitial_construct(self, ctx) : self._insideProc = False

    def enterAlways_construct(self, ctx): self._insideProc = True
    def exitAlways_construct(self, ctx) : self._insideProc = False

    #def _enterProceduceBlock(self, ctx, kw):
    #    try:
    #        name = ctx.statement().procedural_timing_control_statement().statement_or_null().statement().seq_block().block_identifier().getText()
    #    except:
    #        try: name = ctx.statement().seq_block().block_identifier().getText()
    #        except: name = ""
    #    p = self.cont.newProc(kw, name)
    #    self._insideProc = True
    #    self.pushCont(p, ctx)

    def enterBlocking_assignment(self, ctx):
        if not self._insideProc: return
        self._enterNetAssignment(ctx)

    def enterNonblocking_assignment(self, ctx):
        if not self._insideProc: return
        self._enterNetAssignment(ctx)

    def enterCase_statement(self, ctx):
        if not self._insideProc: return
        inferNetsFromExpr(self.cont, ctx.expression())
        for i in ctx.case_item():
            if i.expression():
                for e in i.expression(): inferNetsFromExpr(self.cont, e)

    def enterConditional_statement(self, ctx):
        if not self._insideProc: return
        # statement is infer with children
        inferNetsFromExpr(self.cont, ctx.stat_if().expression())
        if ctx.stat_elseif() != None:
            inferNetsFromExpr(self.cont, ctx.stat_elseif().expression())

    def enterLoop_statement(self, ctx):
        if not self._insideProc: return
        if ctx.expression():
            inferNetsFromExpr(self.cont, ctx.expression())
        if ctx.variable_assignment():
            for a in ctx.variable_assignment():
                self._enterNetAssignment(a)

    def enterEvent_control(self, ctx):
        if not self._insideProc: return
        if ctx.event_expression():
            for e in ctx.event_expression().event_primary():
                inferNetsFromExpr(self.cont, e.expression())

    #def enterSeq_block(self, ctx):


