# Generated from Verex.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by VerexParser.

class VerexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerexParser#vfile.
    def visitVfile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_declaration.
    def visitModule_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#integer_declaration.
    def visitInteger_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#integer_kw.
    def visitInteger_kw(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#HeaderPortName.
    def visitHeaderPortName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#HeaderPortAssign.
    def visitHeaderPortAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_reference.
    def visitPort_reference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_declaration.
    def visitPort_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_identifiers_wrange.
    def visitList_of_port_identifiers_wrange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_identifier_wrange.
    def visitPort_identifier_wrange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#local_parameter_declaration.
    def visitLocal_parameter_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_declaration_.
    def visitParameter_declaration_(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_declaration.
    def visitNet_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_net_identifiers.
    def visitList_of_net_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_identifier_wrange.
    def visitNet_identifier_wrange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_lvalue.
    def visitNet_lvalue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_concatenation_value.
    def visitNet_concatenation_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_lvalue.
    def visitVariable_lvalue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#primary.
    def visitPrimary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierid_reference.
    def visitHierid_reference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#escaped_hierarchical_identifier.
    def visitEscaped_hierarchical_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_hierarchical_identifier.
    def visitSimple_hierarchical_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#conditional_statement.
    def visitConditional_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stat_if.
    def visitStat_if(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stat_elseif.
    def visitStat_elseif(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stat_else.
    def visitStat_else(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_conditional_statement.
    def visitFunction_conditional_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#funct_stat_if.
    def visitFunct_stat_if(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#funct_stat_elseif.
    def visitFunct_stat_elseif(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#funct_stat_else.
    def visitFunct_stat_else(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#arrayed_identifier.
    def visitArrayed_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#regex_arrayed_identifier.
    def visitRegex_arrayed_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_parameter_assignments.
    def visitList_of_parameter_assignments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#equal_parameter_assignment.
    def visitEqual_parameter_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_instance.
    def visitModule_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#special_port_connection.
    def visitSpecial_port_connection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#comma_special_port_connection.
    def visitComma_special_port_connection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_connections.
    def visitList_of_port_connections(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mixed_port_connection.
    def visitMixed_port_connection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#comma_mixed_port_connection.
    def visitComma_mixed_port_connection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_connection_expression.
    def visitPort_connection_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#range_.
    def visitRange_(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#range_expression.
    def visitRange_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#dimension.
    def visitDimension(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#config_declaration.
    def visitConfig_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#design_statement.
    def visitDesign_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#config_rule_statement.
    def visitConfig_rule_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#default_clause.
    def visitDefault_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inst_clause.
    def visitInst_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inst_name.
    def visitInst_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#liblist_clause.
    def visitLiblist_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cell_clause.
    def visitCell_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#use_clause.
    def visitUse_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#source_text.
    def visitSource_text(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#description.
    def visitDescription(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_keyword.
    def visitModule_keyword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_parameter_port_list.
    def visitModule_parameter_port_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_ports.
    def visitList_of_ports(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_declarations.
    def visitList_of_port_declarations(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_expression.
    def visitPort_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_item.
    def visitModule_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_or_generate_item.
    def visitModule_or_generate_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#non_port_module_item.
    def visitNon_port_module_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_or_generate_item_declaration.
    def visitModule_or_generate_item_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_override.
    def visitParameter_override(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_declaration.
    def visitParameter_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specparam_declaration.
    def visitSpecparam_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inout_declaration.
    def visitInout_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_declaration.
    def visitInput_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_declaration.
    def visitOutput_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_declaration.
    def visitEvent_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_declaration.
    def visitGenvar_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#time_declaration.
    def visitTime_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#real_declaration.
    def visitReal_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#realtime_declaration.
    def visitRealtime_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#reg_declaration.
    def visitReg_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_type.
    def visitNet_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_variable_type.
    def visitOutput_variable_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#real_type.
    def visitReal_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_type.
    def visitVariable_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#drive_strength.
    def visitDrive_strength(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#strength0.
    def visitStrength0(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#strength1.
    def visitStrength1(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#charge_strength.
    def visitCharge_strength(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay3.
    def visitDelay3(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay2.
    def visitDelay2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay_value.
    def visitDelay_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_event_identifiers.
    def visitList_of_event_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_genvar_identifiers.
    def visitList_of_genvar_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_identifiers.
    def visitList_of_port_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_net_decl_assignments.
    def visitList_of_net_decl_assignments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_param_assignments.
    def visitList_of_param_assignments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_specparam_assignments.
    def visitList_of_specparam_assignments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_real_identifiers.
    def visitList_of_real_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_variable_identifiers.
    def visitList_of_variable_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_variable_port_identifiers.
    def visitList_of_variable_port_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_decl_assignment.
    def visitNet_decl_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#param_assignment.
    def visitParam_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specparam_assignment.
    def visitSpecparam_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pulse_control_specparam.
    def visitPulse_control_specparam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#error_limit_value.
    def visitError_limit_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#reject_limit_value.
    def visitReject_limit_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#limit_value.
    def visitLimit_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_declaration.
    def visitFunction_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_item_declaration.
    def visitFunction_item_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_port_list.
    def visitFunction_port_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_port.
    def visitFunction_port(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#range_or_type.
    def visitRange_or_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_declaration.
    def visitTask_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_item_declaration.
    def visitTask_item_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_port_list.
    def visitTask_port_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_port_item.
    def visitTask_port_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tf_decl_header.
    def visitTf_decl_header(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tf_declaration.
    def visitTf_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_port_type.
    def visitTask_port_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_item_declaration.
    def visitBlock_item_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_reg_declaration.
    def visitBlock_reg_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_block_variable_identifiers.
    def visitList_of_block_variable_identifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_variable_type.
    def visitBlock_variable_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#gate_instantiation.
    def visitGate_instantiation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cmos_switch_instance.
    def visitCmos_switch_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#enable_gate_instance.
    def visitEnable_gate_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mos_switch_instance.
    def visitMos_switch_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_input_gate_instance.
    def visitN_input_gate_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_output_gate_instance.
    def visitN_output_gate_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_switch_instance.
    def visitPass_switch_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_enable_switch_instance.
    def visitPass_enable_switch_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pull_gate_instance.
    def visitPull_gate_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#name_of_gate_instance.
    def visitName_of_gate_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pulldown_strength.
    def visitPulldown_strength(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pullup_strength.
    def visitPullup_strength(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#enable_terminal.
    def visitEnable_terminal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#ncontrol_terminal.
    def visitNcontrol_terminal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pcontrol_terminal.
    def visitPcontrol_terminal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_terminal.
    def visitInput_terminal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inout_terminal.
    def visitInout_terminal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_terminal.
    def visitOutput_terminal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cmos_switchtype.
    def visitCmos_switchtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#enable_gatetype.
    def visitEnable_gatetype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mos_switchtype.
    def visitMos_switchtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_input_gatetype.
    def visitN_input_gatetype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_output_gatetype.
    def visitN_output_gatetype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_en_switchtype.
    def visitPass_en_switchtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_switchtype.
    def visitPass_switchtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_instantiation.
    def visitModule_instantiation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_value_assignment.
    def visitParameter_value_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#ordered_parameter_assignment.
    def visitOrdered_parameter_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#named_parameter_assignment.
    def visitNamed_parameter_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#name_of_instance.
    def visitName_of_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#ordered_port_connection.
    def visitOrdered_port_connection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#named_port_connection.
    def visitNamed_port_connection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generated_instantiation.
    def visitGenerated_instantiation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_item_or_null.
    def visitGenerate_item_or_null(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_item.
    def visitGenerate_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_conditional_statement.
    def visitGenerate_conditional_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_case_statement.
    def visitGenerate_case_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_case_item.
    def visitGenvar_case_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_loop_statement.
    def visitGenerate_loop_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_assignment.
    def visitGenvar_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_block.
    def visitGenerate_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#continuous_assign.
    def visitContinuous_assign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_net_assignments.
    def visitList_of_net_assignments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_assignment.
    def visitNet_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#initial_construct.
    def visitInitial_construct(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#always_construct.
    def visitAlways_construct(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#blocking_assignment.
    def visitBlocking_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#nonblocking_assignment.
    def visitNonblocking_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#procedural_continuous_assignments.
    def visitProcedural_continuous_assignments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_blocking_assignment.
    def visitFunction_blocking_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_statement_or_null.
    def visitFunction_statement_or_null(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_seq_block.
    def visitFunction_seq_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_assignment.
    def visitVariable_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#par_block.
    def visitPar_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#seq_block.
    def visitSeq_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#statement_or_null.
    def visitStatement_or_null(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_statement.
    def visitFunction_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay_or_event_control.
    def visitDelay_or_event_control(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay_control.
    def visitDelay_control(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#disable_statement.
    def visitDisable_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_control.
    def visitEvent_control(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_trigger.
    def visitEvent_trigger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_expression.
    def visitEvent_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_primary.
    def visitEvent_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#procedural_timing_control_statement.
    def visitProcedural_timing_control_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#wait_statement.
    def visitWait_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#if_else_if_statement.
    def visitIf_else_if_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_if_else_if_statement.
    def visitFunction_if_else_if_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#case_statement.
    def visitCase_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#case_item.
    def visitCase_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_case_statement.
    def visitFunction_case_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_case_item.
    def visitFunction_case_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_loop_statement.
    def visitFunction_loop_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#loop_statement.
    def visitLoop_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_task_enable.
    def visitSystem_task_enable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_enable.
    def visitTask_enable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_block.
    def visitSpecify_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_item.
    def visitSpecify_item(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pulsestyle_declaration.
    def visitPulsestyle_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#showcancelled_declaration.
    def visitShowcancelled_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#path_declaration.
    def visitPath_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_path_declaration.
    def visitSimple_path_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parallel_path_description.
    def visitParallel_path_description(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#full_path_description.
    def visitFull_path_description(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_path_inputs.
    def visitList_of_path_inputs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_path_outputs.
    def visitList_of_path_outputs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_input_terminal_descriptor.
    def visitSpecify_input_terminal_descriptor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_output_terminal_descriptor.
    def visitSpecify_output_terminal_descriptor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_identifier.
    def visitInput_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_identifier.
    def visitOutput_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#path_delay_value.
    def visitPath_delay_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_path_delay_expressions.
    def visitList_of_path_delay_expressions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t_path_delay_expression.
    def visitT_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#trise_path_delay_expression.
    def visitTrise_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tfall_path_delay_expression.
    def visitTfall_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tz_path_delay_expression.
    def visitTz_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t01_path_delay_expression.
    def visitT01_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t10_path_delay_expression.
    def visitT10_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t0z_path_delay_expression.
    def visitT0z_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tz1_path_delay_expression.
    def visitTz1_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t1z_path_delay_expression.
    def visitT1z_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tz0_path_delay_expression.
    def visitTz0_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t0x_path_delay_expression.
    def visitT0x_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tx1_path_delay_expression.
    def visitTx1_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t1x_path_delay_expression.
    def visitT1x_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tx0_path_delay_expression.
    def visitTx0_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#txz_path_delay_expression.
    def visitTxz_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tzx_path_delay_expression.
    def visitTzx_path_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#path_delay_expression.
    def visitPath_delay_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#edge_sensitive_path_declaration.
    def visitEdge_sensitive_path_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parallel_edge_sensitive_path_description.
    def visitParallel_edge_sensitive_path_description(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#full_edge_sensitive_path_description.
    def visitFull_edge_sensitive_path_description(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#data_source_expression.
    def visitData_source_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#edge_identifier.
    def visitEdge_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#state_dependent_path_declaration.
    def visitState_dependent_path_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#polarity_operator.
    def visitPolarity_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#checktime_condition.
    def visitChecktime_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delayed_data.
    def visitDelayed_data(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delayed_reference.
    def visitDelayed_reference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#end_edge_offset.
    def visitEnd_edge_offset(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_based_flag.
    def visitEvent_based_flag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#notify_reg.
    def visitNotify_reg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#remain_active_flag.
    def visitRemain_active_flag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stamptime_condition.
    def visitStamptime_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#start_edge_offset.
    def visitStart_edge_offset(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#threshold.
    def visitThreshold(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#timing_check_limit.
    def visitTiming_check_limit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#concatenation.
    def visitConcatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_concatenation.
    def visitConstant_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_multiple_concatenation.
    def visitConstant_multiple_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_concatenation.
    def visitModule_path_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_multiple_concatenation.
    def visitModule_path_multiple_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#multiple_concatenation.
    def visitMultiple_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_concatenation.
    def visitNet_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_concatenation.
    def visitVariable_concatenation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_concatenation_value.
    def visitVariable_concatenation_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_function_call.
    def visitConstant_function_call(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_call.
    def visitFunction_call(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_function_call.
    def visitSystem_function_call(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_function_call.
    def visitGenvar_function_call(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#base_expression.
    def visitBase_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_base_expression.
    def visitConstant_base_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_expression.
    def visitConstant_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_mintypmax_expression.
    def visitConstant_mintypmax_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_range_expression.
    def visitConstant_range_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#dimension_constant_expression.
    def visitDimension_constant_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#lsb_constant_expression.
    def visitLsb_constant_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mintypmax_expression.
    def visitMintypmax_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_conditional_expression.
    def visitModule_path_conditional_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_expression.
    def visitModule_path_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_mintypmax_expression.
    def visitModule_path_mintypmax_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#msb_constant_expression.
    def visitMsb_constant_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#width_constant_expression.
    def visitWidth_constant_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_primary.
    def visitConstant_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_primary.
    def visitModule_path_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#unary_operator.
    def visitUnary_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#binary_operator.
    def visitBinary_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#unary_module_path_operator.
    def visitUnary_module_path_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#binary_module_path_operator.
    def visitBinary_module_path_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#timing_spec.
    def visitTiming_spec(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#attribute_instance.
    def visitAttribute_instance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#attr_spec.
    def visitAttr_spec(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#attr_name.
    def visitAttr_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_identifier.
    def visitBlock_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cell_identifier.
    def visitCell_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#config_identifier.
    def visitConfig_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#escaped_arrayed_identifier.
    def visitEscaped_arrayed_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_identifier.
    def visitEvent_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_identifier.
    def visitFunction_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#gate_instance_identifier.
    def visitGate_instance_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_block_identifier.
    def visitGenerate_block_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_function_identifier.
    def visitGenvar_function_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_identifier.
    def visitGenvar_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_block_identifier.
    def visitHierarchical_block_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_event_identifier.
    def visitHierarchical_event_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_function_identifier.
    def visitHierarchical_function_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_net_identifier.
    def visitHierarchical_net_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_variable_identifier.
    def visitHierarchical_variable_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_task_identifier.
    def visitHierarchical_task_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inout_port_identifier.
    def visitInout_port_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_port_identifier.
    def visitInput_port_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#instance_identifier.
    def visitInstance_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#library_identifier.
    def visitLibrary_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#memory_identifier.
    def visitMemory_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_identifier.
    def visitModule_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_instance_identifier.
    def visitModule_instance_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_identifier.
    def visitNet_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_port_identifier.
    def visitOutput_port_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_identifier.
    def visitParameter_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_identifier.
    def visitPort_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#real_identifier.
    def visitReal_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_arrayed_identifier.
    def visitSimple_arrayed_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specparam_identifier.
    def visitSpecparam_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_function_identifier.
    def visitSystem_function_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_task_identifier.
    def visitSystem_task_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_identifier.
    def visitTask_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#terminal_identifier.
    def visitTerminal_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_identifier.
    def visitText_macro_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#topmodule_identifier.
    def visitTopmodule_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#udp_identifier.
    def visitUdp_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#udp_instance_identifier.
    def visitUdp_instance_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_identifier.
    def visitVariable_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_hierarchical_branch.
    def visitSimple_hierarchical_branch(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#escaped_hierarchical_branch.
    def visitEscaped_hierarchical_branch(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_definition.
    def visitText_macro_definition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_name.
    def visitText_macro_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_formal_arguments.
    def visitList_of_formal_arguments(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#formal_argument_identifier.
    def visitFormal_argument_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#macro_text.
    def visitMacro_text(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_usage.
    def visitText_macro_usage(self, ctx):
        return self.visitChildren(ctx)


