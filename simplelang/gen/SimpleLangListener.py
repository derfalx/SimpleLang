# Generated from C:/Users/falx/PycharmProjects/SimpleLang\SimpleLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#code.
    def enterCode(self, ctx:SimpleLangParser.CodeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#code.
    def exitCode(self, ctx:SimpleLangParser.CodeContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#expr.
    def enterExpr(self, ctx:SimpleLangParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#expr.
    def exitExpr(self, ctx:SimpleLangParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#arithmetic_expr.
    def enterArithmetic_expr(self, ctx:SimpleLangParser.Arithmetic_exprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#arithmetic_expr.
    def exitArithmetic_expr(self, ctx:SimpleLangParser.Arithmetic_exprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#bool_expr.
    def enterBool_expr(self, ctx:SimpleLangParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#bool_expr.
    def exitBool_expr(self, ctx:SimpleLangParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
        pass



del SimpleLangParser