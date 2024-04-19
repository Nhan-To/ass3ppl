# Generated from c://Users//HP//Downloads//assignment3-initial-real//assignment3-initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body.
    def enterBody(self, ctx:ZCodeParser.BodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body.
    def exitBody(self, ctx:ZCodeParser.BodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#number_literal.
    def enterNumber_literal(self, ctx:ZCodeParser.Number_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#number_literal.
    def exitNumber_literal(self, ctx:ZCodeParser.Number_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrprm.
    def enterArrprm(self, ctx:ZCodeParser.ArrprmContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrprm.
    def exitArrprm(self, ctx:ZCodeParser.ArrprmContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lhs.
    def enterLhs(self, ctx:ZCodeParser.LhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lhs.
    def exitLhs(self, ctx:ZCodeParser.LhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variables.
    def enterVariables(self, ctx:ZCodeParser.VariablesContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variables.
    def exitVariables(self, ctx:ZCodeParser.VariablesContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implicit.
    def enterImplicit(self, ctx:ZCodeParser.ImplicitContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implicit.
    def exitImplicit(self, ctx:ZCodeParser.ImplicitContext):
        pass


    # Enter a parse tree produced by ZCodeParser#keyword.
    def enterKeyword(self, ctx:ZCodeParser.KeywordContext):
        pass

    # Exit a parse tree produced by ZCodeParser#keyword.
    def exitKeyword(self, ctx:ZCodeParser.KeywordContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dynamic.
    def enterDynamic(self, ctx:ZCodeParser.DynamicContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dynamic.
    def exitDynamic(self, ctx:ZCodeParser.DynamicContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func.
    def enterFunc(self, ctx:ZCodeParser.FuncContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func.
    def exitFunc(self, ctx:ZCodeParser.FuncContext):
        pass


    # Enter a parse tree produced by ZCodeParser#prm.
    def enterPrm(self, ctx:ZCodeParser.PrmContext):
        pass

    # Exit a parse tree produced by ZCodeParser#prm.
    def exitPrm(self, ctx:ZCodeParser.PrmContext):
        pass


    # Enter a parse tree produced by ZCodeParser#prm_list.
    def enterPrm_list(self, ctx:ZCodeParser.Prm_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#prm_list.
    def exitPrm_list(self, ctx:ZCodeParser.Prm_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dclr_stmt.
    def enterDclr_stmt(self, ctx:ZCodeParser.Dclr_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dclr_stmt.
    def exitDclr_stmt(self, ctx:ZCodeParser.Dclr_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ass_stmt.
    def enterAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ass_stmt.
    def exitAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assign_lhs.
    def enterAssign_lhs(self, ctx:ZCodeParser.Assign_lhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assign_lhs.
    def exitAssign_lhs(self, ctx:ZCodeParser.Assign_lhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_dimension.
    def enterArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_dimension.
    def exitArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_stmt.
    def enterIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_stmt.
    def exitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_stmt.
    def enterElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_stmt.
    def exitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_stmt.
    def enterFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_stmt.
    def exitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_stmt.
    def enterBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_stmt.
    def exitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#cont_stmt.
    def enterCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#cont_stmt.
    def exitCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_stmt.
    def enterReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_stmt.
    def exitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#call_stmt.
    def enterCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#call_stmt.
    def exitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_list.
    def enterStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_list.
    def exitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_stmt.
    def enterBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_stmt.
    def exitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_rela.
    def enterExpr_rela(self, ctx:ZCodeParser.Expr_relaContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_rela.
    def exitExpr_rela(self, ctx:ZCodeParser.Expr_relaContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_log.
    def enterExpr_log(self, ctx:ZCodeParser.Expr_logContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_log.
    def exitExpr_log(self, ctx:ZCodeParser.Expr_logContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_add.
    def enterExpr_add(self, ctx:ZCodeParser.Expr_addContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_add.
    def exitExpr_add(self, ctx:ZCodeParser.Expr_addContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_mul.
    def enterExpr_mul(self, ctx:ZCodeParser.Expr_mulContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_mul.
    def exitExpr_mul(self, ctx:ZCodeParser.Expr_mulContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_not.
    def enterExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_not.
    def exitExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_sign.
    def enterExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_sign.
    def exitExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_idx.
    def enterExpr_idx(self, ctx:ZCodeParser.Expr_idxContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_idx.
    def exitExpr_idx(self, ctx:ZCodeParser.Expr_idxContext):
        pass


    # Enter a parse tree produced by ZCodeParser#idx_lhs.
    def enterIdx_lhs(self, ctx:ZCodeParser.Idx_lhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#idx_lhs.
    def exitIdx_lhs(self, ctx:ZCodeParser.Idx_lhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_var.
    def enterExpr_var(self, ctx:ZCodeParser.Expr_varContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_var.
    def exitExpr_var(self, ctx:ZCodeParser.Expr_varContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_expr.
    def enterList_expr(self, ctx:ZCodeParser.List_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_expr.
    def exitList_expr(self, ctx:ZCodeParser.List_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_literal.
    def enterList_literal(self, ctx:ZCodeParser.List_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_literal.
    def exitList_literal(self, ctx:ZCodeParser.List_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr_expr.
    def enterArr_expr(self, ctx:ZCodeParser.Arr_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr_expr.
    def exitArr_expr(self, ctx:ZCodeParser.Arr_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr_lit.
    def enterArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr_lit.
    def exitArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ignore.
    def enterIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ignore.
    def exitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass


    # Enter a parse tree produced by ZCodeParser#cmt_list.
    def enterCmt_list(self, ctx:ZCodeParser.Cmt_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#cmt_list.
    def exitCmt_list(self, ctx:ZCodeParser.Cmt_listContext):
        pass



del ZCodeParser