# Generated from C:/Users/falx/PycharmProjects/SimpleLang\SimpleLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#code.
    def visitCode(self, ctx:SimpleLangParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#expr.
    def visitExpr(self, ctx:SimpleLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#arithmetic_expr.
    def visitArithmetic_expr(self, ctx:SimpleLangParser.Arithmetic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#bool_expr.
    def visitBool_expr(self, ctx:SimpleLangParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)



del SimpleLangParser