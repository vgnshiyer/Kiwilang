from antlr4 import *

from lexer_and_parser.KiwiParser import KiwiParser
from lexer_and_parser.KiwiVisitor import KiwiVisitor

# This class defines a complete generic visitor for a parse tree produced by KiwiParser.

DEBUG_LEVEL = False

class KiwiInterpreter(KiwiVisitor):

    env = None

    class variable:
        vartype = None
        var = None
        val = None

    # Visit a parse tree produced by KiwiParser#program.
    def visitProgram(self, ctx:KiwiParser.ProgramContext):
        self.env = {}
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
            vartype = children[0].getText()
            var = children[1].getText()
            val = self.visit(children[3])
            self.updateEnv(var, val, vartype)
        elif len(children) == 3:
            var = children[0].getText()
            val = self.visit(children[2])
            vartype = str(type(val).__name__)
            self.updateEnv(var, val, vartype)
        elif len(children) == 2:
            newvar = self.variable()
            vartype = children[0].getText()
            var = children[1].getText()
            self.updateEnv(var, None, vartype)
        else:
            raise Exception('Invalid declaration expression.')
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
        children = ctx.children
        if len(children)==2:
            var = children[1].getText()
            if(var in self.env):
                varVal = self.env[var].val
                print(varVal)
            else:
                raise Exception('Variable not preset: variable {} is not defined'.format(var))
        else:
            raise Exception('print accepts only one argument.')
        
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
        for v in self.env.values():
            print('-'*50)
            print(v.vartype)
            print(v.var)
            print(v.val)
    
    def updateEnv(self,var,val,vartype):
        if var in self.env:
            variable = self.env[var]
            if(variable.vartype != str(type(val).__name__)):
                raise Exception('Invalid type assigned: {} of type {} cannot be assigned to {} of type {}'.format(val, str(type(val)), var, vartype))
            else:
                variable.val = val
        else:
            if(vartype != type(val).__name__ and val != None):
                raise Exception('Invalid type assigned: {} of type {} cannot be assigned to {} of type {}'.format(val, str(type(val)), var, vartype))
            newvar = self.variable()
            newvar.var = var
            newvar.val = val
            newvar.vartype = vartype
            self.env[var] = newvar