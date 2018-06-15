
from __future__ import print_function, absolute_import
from .IOAnalyzer import *

_defaultNodes = """
    vfile description
        =module_declaration
            module_parameter_port_list
                =parameter_declaration_
            ==list_of_ports
                #accept_this
            list_of_port_declarations
                =port_declaration
            module_item non_port_module_item
                parameter_declaration
                    =parameter_declaration_
                =local_parameter_declaration
                ?generated_instantiation
                module_or_generate_item
                    module_or_generate_item_declaration
                        >net_declaration
                        =reg_declaration
                    >>continuous_assign
                        #accept_all_this
                    >module_instantiation
                        list_of_port_connections
                            ?ordered_port_connection #not_supported
                            >mixed_port_connection >comma_mixed_port_connection
                    >initial_construct
                        #...statement
                    >always_construct
                        #...statement
                !...
                    statement_or_null
                    statement    #only_these_kind_is_visit
                        >blocking_assignment
                        >case_statement
                        >>conditional_statement
                            #sub_cond_stat_...
                        >loop_statement
                        >nonblocking_assignment
                        >procedural_timing_control_statement
                            !... >>event_control
                        >>seq_block
                !...
                    >>expression
                        >>term  #sometime_you_want_to_use_visitChilds(expression)
                        #expression_need_to_be_accepted_from_upper_level
"""

class ModuleAnalyzer(IOAnalyzer):
    def __init__(self, vunit=None, options=None):
        super(ModuleAnalyzer, self).__init__(vunit, options)
        self._visitChildNodes.update(initDefaultChild(_defaultNodes))
        self.unit = curCont().getRoot()
        #from verilog.Unit import Unit
        #self.unit = curCont()
        #for i in range(1000000):
        #    if isinstance(self.unit, Unit):
        #        break
        #    self.unit = self.unit.parent
        #if not isinstance(self.unit, Unit):
        #    raise InternalFatal("Cannot find root Unit")

    # net decl, IO dont go and check assignment
    def visitNet_declaration(self, ctx):
        nt = ctx.net_type().getText() if ctx.net_type() else ctx.regtype.text
        parr = range2arr(ctx.range_())
        if ctx.list_of_net_identifiers() != None:
            for nctx in ctx.list_of_net_identifiers().net_identifier_wrange():
                n = curCont().newNet(nctx.net_identifier().getText(), nt)
                n.declBus(parr, dim2arr(nctx.dimension()))
        else:
            for nctx in ctx.list_of_net_decl_assignments().net_decl_assignment():
                n = curCont().newNet(nctx.net_identifier().getText(), nt)
                n.declBus(parr)
                pushCont( curCont().newAssign('decl_assign') )
                curCont().referNet(n.name, parr)
                curCont().setRhs()
                self.visitChilds(nctx.expression())
                popCont()

    def visitHierid_reference(self, ctx):
        refbus = []
        for e in ctx.expression(): refbus.append( [e.getText()]*2 )
        if ctx.range_expression():
            refbus.append(rexpr2arr(ctx.range_expression()))
        curCont().referNet(ctx.hierarchical_identifier().getText(), refbus)

    # assignment
    def _visitAssigment(self, ctx, ntype):
        try: lhs = ctx.variable_lvalue()
        except: lhs = ctx.net_lvalue()
        a = pushCont(curCont().newAssign(ntype))
        self.visitChilds(lhs)
        a.setRhs()
        self.visitChilds(ctx.expression())
        popCont()

    def visitNet_assignment(self, ctx):
        self._visitAssigment(ctx, 'cont_assign')

    # cell instance/parameter override
    def visitModule_instantiation(self, ctx):
        name = self._savedctx['modname'] = ctx.module_identifier().getText()
        #if name not in self.unit.mods:
        #    fname = self.opts.findFile(name)
        self.visitChilds(ctx)

    def visitList_of_parameter_assignments(self, ctx):
        self._savedctx['param_o'] = []
        self._savedctx['param_n'] = {}
        self.visitChilds(ctx)

    def visitOrdered_parameter_assignment(self, ctx):
        self._savedctx['param_o'].append(ctx.expression().getText())

    def visitNamed_parameter_assignment(self, ctx):
        self._savedctx['param_n'][ctx.parameter_identifier().getText()] = \
                ctx.expression().getText()

    def visitEqual_parameter_assignment(self, ctx):
        self.visitNamed_parameter_assignment(ctx)

    def visitModule_instance(self, ctx):
        m = curCont().newCell(ctx.name_of_instance().getText(),
                            self._savedctx['modname'])
        m.defparams(self._savedctx['param_o'])
        m.defparams(self._savedctx['param_n'])
        pushCont(m)
        self.visitChilds(ctx)
        popCont()

    def visitSpecial_port_connection(self,ctx):
        p = curCont().newPin('/*/')
        p.referNet(ctx.getText()[1])

    def visitComma_Special_port_connection(self, ctx):
        self.visitChilds(ctx)

    # dont infer ordered port connection for now
    def visitMixed_port_connection(self, ctx):
        dir_ = 'any'
        if ctx.PinDirection:
            dir_ =  ctx.PinDirection.text
            if 'put' not in dir_ and dir_ != 'any':
                dir_ += 'put'
        p = curCont().newPin(ctx.port_identifier().getText(), dir_)
        if ctx.port_connection_expression():
            pushCont(p)
            self.visitChilds(ctx.port_connection_expression())
            popCont()

    def visitComma_mixed_port_connection(self, ctx):
        self.visitChilds(ctx)
        

    ## proceduce block
    def visitInitial_construct(self, ctx):
        pushCont(curCont().newSeq('initial'))
        self.visitChilds(ctx)
        popCont()

    def visitAlways_construct(self, ctx):
        pushCont(curCont().newSeq('always'))
        self.visitChilds(ctx)
        popCont()

    def visitBlocking_assignment(self, ctx):
        self._visitAssigment(ctx, 'blocking')

    def visitNonblocking_assignment(self, ctx):
        self._visitAssigment(ctx, 'nonblock')

    def visitCase_statement(self, ctx):
        pushCont(curCont().newOtherRhs('__case_expression__'))
        self.visitChilds(ctx.expression())
        popCont()
        for i in ctx.case_item():
            pushCont(curCont().newOtherRhs('__case_item__'))
            for e in i.expression():
                self.visitChilds(e)
            popCont()
            self.visitChilds(i.statement_or_null())

    def visitStat_if(self, ctx):
        pushCont(curCont().newOtherRhs('__if_cond__'))
        self.visitChilds(ctx.expression())
        popCont()
        self.visitChilds(ctx.statement_or_null())

    def visitStat_elseif(self, ctx):
        self.visitStat_if(ctx)

    def visitStat_else(self, ctx):
        self.visitChilds(ctx.statement_or_null())

    def visitLoop_statement(self, ctx):
        for a in ctx.variable_assignment():
            self._visitAssignment(a, 'loop_assign')
        if ctx.expression():
            pushCont(curCont().newOtherRhs('__loop_cond__'))
            self.visitChilds(ctx.expression())
            popCont()
        self.visitChilds(ctx.statement)

    def visitProcedural_timing_control_statement(self, ctx):
        if ctx.delay_or_event_control().event_control():
            pushCont(curCont().newOtherRhs('__event_control__'))
            self.visitChilds(ctx.delay_or_event_control())
            popCont()
        self.visitChilds(ctx.statement_or_null())



