# Generated from Kiwi.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KiwiParser import KiwiParser
else:
    from KiwiParser import KiwiParser

# This class defines a complete generic visitor for a parse tree produced by KiwiParser.

DEBUG_LEVEL = False

class KiwiVisitor(ParseTreeVisitor):

    env = None

    class variable:
        vartype = None
        var = None
        val = None

    # Visit a parse tree produced by KiwiParser#program.
    def visitProgram(self, ctx:KiwiParser.ProgramContext):
        self.env = set()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#block.
    def visitBlock(self, ctx:KiwiParser.BlockContext):
        if(DEBUG_LEVEL):
            print('visitBlock: ' + ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#statement.
    def visitStatement(self, ctx:KiwiParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#declaration.
    def visitDeclaration(self, ctx:KiwiParser.DeclarationContext):
        
        children = ctx.children
        if len(children) == 4:
            newvar = self.variable()
            newvar.vartype = children[0].getText()
            newvar.var = children[1].getText()
            newvar.val = self.visit(children[3])
            # if(str(type(val)) != newvar.vartype):
            #     raise Exception('Invalid datatype: `{}` of type {} cannot be stored in `{}` of type {}'.format(str(val), str(type(val)), str(var), str(type_)))
            self.env.add(newvar)
        elif len(children) == 3:
            newvar = self.variable()
            newvar.vartype = 'any'
            newvar.var = children[0].getText()
            newvar.val = self.visit(children[2])
            self.env.add(newvar)
        elif len(children) == 2:
            newvar = self.variable()
            newvar.vartype = children[0].getText()
            newvar.var = children[1].getText()
            self.env.add(newvar)
        if(DEBUG_LEVEL): self.printEnv()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#incrementExpr.
    def visitIncrementExpr(self, ctx:KiwiParser.IncrementExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:KiwiParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#booleanExpr.
    def visitBooleanExpr(self, ctx:KiwiParser.BooleanExprContext):
        if(DEBUG_LEVEL):
            print('visitBoolean: ')
            print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#ifExpr.
    def visitIfExpr(self, ctx:KiwiParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#elseIfExpr.
    def visitElseIfExpr(self, ctx:KiwiParser.ElseIfExprContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#whileExpr.
    def visitWhileExpr(self, ctx:KiwiParser.WhileExprContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#forExpr.
    def visitForExpr(self, ctx:KiwiParser.ForExprContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#specialForExpr.
    def visitSpecialForExpr(self, ctx:KiwiParser.SpecialForExprContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#display.
    def visitDisplay(self, ctx:KiwiParser.DisplayContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#function.
    def visitFunction(self, ctx:KiwiParser.FunctionContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#params.
    def visitParams(self, ctx:KiwiParser.ParamsContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#give.
    def visitGive(self, ctx:KiwiParser.GiveContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#functionCall.
    def visitFunctionCall(self, ctx:KiwiParser.FunctionCallContext):
        if(DEBUG_LEVEL): print(ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by KiwiParser#stringExpr.
    def visitStringExpr(self, ctx:KiwiParser.StringExprContext):
        return str(ctx.getText().replace('"',''))

    def printEnv(self):
        for v in self.env:
            print('-'*50)
            print(v.vartype)
            print(v.var)
            print(v.val)

del KiwiParser