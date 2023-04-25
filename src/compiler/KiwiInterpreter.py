'''
Author: Vignesh Iyer, Dharani Chinta
Version: 1
Date: April 23th 2023
'''

# references: https://dev.to/taw/100-languages-speedrun-episode-74-python-antlr-4-234l
#             https://codereview.stackexchange.com/questions/280439/interpreter-for-a-python-like-language-antlr-and-python

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

    exprEval = {
        '+' : lambda a, b: a + b,
        '-' : lambda a, b: a - b,
        '*' : lambda a, b: a * b,
        '/' : lambda a, b: a // b,
        '==' : lambda a, b: a == b,
        '!=' : lambda a, b: a != b,
        'and' : lambda a, b: a and b,
        'or' : lambda a, b: a or b,
        '>' : lambda a, b: a > b,
        '<' : lambda a, b: a < b,
        '<=' : lambda a, b: a <= b,
        '>=' : lambda a, b: a >= b
    }

    def printEnv(self):
        for v in self.env.values():
            print('-'*50)
            print(v.vartype)
            print(v.var)
            print(v.val)
        print('-'*50)
    
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

    def lookup(self, varname):
        if varname in self.env:
            return self.env[varname].val
        else:
            raise Exception('Variable not present: Variable {} does not exist'.format(varname))

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
        children = ctx.children
        if len(children) == 2:
            var = children[0].getText()
            if(var in self.env):
                variable = self.env[var]
                if(variable.vartype == 'int'):
                    op = children[1].getText()
                    if(op == '++'):
                        variable.val += 1
                    elif(op == '--'):
                        variable.val -= 1
                    self.updateEnv(variable.var, variable.val, variable.vartype)
                else: raise Exception('Invalid datatype for operation: Cannot perform arithmetic operations on type {}'.format(variable.vartype))
            else:
                raise Exception('Variable not present: variable {} is not defined'.format(var))

        elif len(children) == 4:
            var = children[0].getText()

            if(var in self.env):
                variable = self.env[var]
                if(variable.vartype == 'int'):
                    op = children[1].getText()
                    val = self.visit(children[3])
                    
                    if op == '+':
                        variable.val += val
                    elif op == '-':
                        variable.val -= val
                    elif op == '*':
                        variable.val *= val
                    elif op == '/':
                        variable.val //= val 
                    self.updateEnv(variable.var, variable.val, variable.vartype)
                else: raise Exception('Invalid datatype for operation: Cannot perform arithmetic operations on type {}'.format(variable.vartype))
            else:
                raise Exception('Variable not present: variable {} is not defined'.format(var))

        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:KiwiParser.ArithmeticExprContext):
        children = ctx.children
        if len(children) == 1:
            if children[0].getText() == 'functionCall':
                pass # handle later
            elif children[0].getSymbol().type == KiwiParser.DIGIT:
                return int(children[0].getText())
            elif children[0].getSymbol().type == KiwiParser.ID:
                return self.lookup(children[0].getText())
        elif len(children) == 2:
            if children[0].getSymbol().type == KiwiParser.SUB:
                if children[1].getSymbol().type == KiwiParser.DIGIT:
                    val = 0 - int(children[1].getText())
                    return val
                elif children[1].getSymbol().type == KiwiParser.ID:
                    val = self.lookup(children[1].getText())
                    if type(val).__name__ != 'int':
                        raise Exception('Invalid operand used: val of type {} cannot be negated'.format(type(val).__name__))
                    return 0 - val
            else:
                raise Exception('Invalid operand')
        elif len(children) == 3:
            if children[0].getText() == '(':
                return self.visit(children[1])

            op1 = self.visit(children[0])
            op2 = self.visit(children[2])
            op = children[1].getText()

            if op in self.exprEval:
                return self.exprEval[op](op1, op2)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#booleanExpr.
    def visitBooleanExpr(self, ctx:KiwiParser.BooleanExprContext):
        children = ctx.children
        if len(children) == 1:
            if children[0].getText() == 'true':
                return True
            elif children[0].getText() == 'false':
                return False
            elif children[0].getSymbol().type == KiwiParser.ID:
                return self.lookup(children[0].getText())
            else:
                return self.visit(children)
        elif len(children) == 2:
            if children[1].getText() == 'true':
                return False
            elif children[1].getText() == 'false':
                return True
            elif children[1].getSymbol().type == KiwiParser.ID:
                return not self.lookup(children[1].getText())
        elif len(children) == 3:
            if children[0].getText() == '(':
                return self.visit(children[1])

            op1 = self.visit(children[0])
            op = children[1].getText()
            op2 = self.visit(children[2])

            if op in self.exprEval:
                return self.exprEval[op](op1, op2)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KiwiParser#condExpr.
    def visitCondExpr(self, ctx:KiwiParser.CondExprContext):
        children = ctx.children
        if self.visit(children[0]):
            return
        i = 1
        while(i < len(children) and isinstance(children[i], KiwiParser.ElseIfExprContext)):
            res = self.visit(children[i])
            i += 1
            if(res == True): return
        
        if(i < len(children)):
            self.visit(children[i])

    # Visit a parse tree produced by KiwiParser#ifExpr.
    def visitIfExpr(self, ctx:KiwiParser.IfExprContext):
        children = ctx.children
        if(self.visit(children[1])):
            self.visit(children[3])
            return True
        return False
        

    # Visit a parse tree produced by KiwiParser#elseIfExpr.
    def visitElseIfExpr(self, ctx:KiwiParser.ElseIfExprContext):
        children = ctx.children
        if(self.visit(children[1])):
            self.visit(children[3])
            return True
        return False

    # Visit a parse tree produced by KiwiParser#elseExpr.
    def visitElseExpr(self, ctx:KiwiParser.ElseExprContext):
        children = ctx.children
        self.visit(children[2])

    # Visit a parse tree produced by KiwiParser#whileExpr.
    def visitWhileExpr(self, ctx:KiwiParser.WhileExprContext):
        children = ctx.children
        boolExpression = children[1]
        block = children[3]
        while(self.visit(boolExpression)):
            self.visit(block)


    # Visit a parse tree produced by KiwiParser#forExpr.
    def visitForExpr(self, ctx:KiwiParser.ForExprContext):
        children = ctx.children
        declaration = children[2]
        boolExpression = children[4]
        expression = children[6]
        block = children[9]

        self.visit(declaration)
        while(self.visit(boolExpression)):
            self.visit(block)
            self.visit(expression)

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
                raise Exception('Variable not present: variable {} is not defined'.format(var))
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