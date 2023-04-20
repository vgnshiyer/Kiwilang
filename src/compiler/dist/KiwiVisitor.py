# Generated from Kiwi.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KiwiParser import KiwiParser
else:
    from KiwiParser import KiwiParser

# This class defines a complete generic visitor for a parse tree produced by KiwiParser.

class KiwiVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KiwiParser#program.
    def visitProgram(self, ctx:KiwiParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#block.
    def visitBlock(self, ctx:KiwiParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#statement.
    def visitStatement(self, ctx:KiwiParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#declaration.
    def visitDeclaration(self, ctx:KiwiParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#incrementExpr.
    def visitIncrementExpr(self, ctx:KiwiParser.IncrementExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:KiwiParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#booleanExpr.
    def visitBooleanExpr(self, ctx:KiwiParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#ifExpr.
    def visitIfExpr(self, ctx:KiwiParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#elseIfExpr.
    def visitElseIfExpr(self, ctx:KiwiParser.ElseIfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#whileExpr.
    def visitWhileExpr(self, ctx:KiwiParser.WhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#forExpr.
    def visitForExpr(self, ctx:KiwiParser.ForExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#specialForExpr.
    def visitSpecialForExpr(self, ctx:KiwiParser.SpecialForExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#display.
    def visitDisplay(self, ctx:KiwiParser.DisplayContext):
        return self.visitChildren(ctx)



del KiwiParser