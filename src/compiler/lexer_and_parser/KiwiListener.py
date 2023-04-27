# Generated from Kiwi.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KiwiParser import KiwiParser
else:
    from KiwiParser import KiwiParser

# This class defines a complete listener for a parse tree produced by KiwiParser.
class KiwiListener(ParseTreeListener):

    # Enter a parse tree produced by KiwiParser#program.
    def enterProgram(self, ctx:KiwiParser.ProgramContext):
        pass

    # Exit a parse tree produced by KiwiParser#program.
    def exitProgram(self, ctx:KiwiParser.ProgramContext):
        pass


    # Enter a parse tree produced by KiwiParser#block.
    def enterBlock(self, ctx:KiwiParser.BlockContext):
        pass

    # Exit a parse tree produced by KiwiParser#block.
    def exitBlock(self, ctx:KiwiParser.BlockContext):
        pass


    # Enter a parse tree produced by KiwiParser#statement.
    def enterStatement(self, ctx:KiwiParser.StatementContext):
        pass

    # Exit a parse tree produced by KiwiParser#statement.
    def exitStatement(self, ctx:KiwiParser.StatementContext):
        pass


    # Enter a parse tree produced by KiwiParser#declaration.
    def enterDeclaration(self, ctx:KiwiParser.DeclarationContext):
        pass

    # Exit a parse tree produced by KiwiParser#declaration.
    def exitDeclaration(self, ctx:KiwiParser.DeclarationContext):
        pass


    # Enter a parse tree produced by KiwiParser#incrementExpr.
    def enterIncrementExpr(self, ctx:KiwiParser.IncrementExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#incrementExpr.
    def exitIncrementExpr(self, ctx:KiwiParser.IncrementExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:KiwiParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:KiwiParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#booleanExpr.
    def enterBooleanExpr(self, ctx:KiwiParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#booleanExpr.
    def exitBooleanExpr(self, ctx:KiwiParser.BooleanExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#condExpr.
    def enterCondExpr(self, ctx:KiwiParser.CondExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#condExpr.
    def exitCondExpr(self, ctx:KiwiParser.CondExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#ifExpr.
    def enterIfExpr(self, ctx:KiwiParser.IfExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#ifExpr.
    def exitIfExpr(self, ctx:KiwiParser.IfExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#elseIfExpr.
    def enterElseIfExpr(self, ctx:KiwiParser.ElseIfExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#elseIfExpr.
    def exitElseIfExpr(self, ctx:KiwiParser.ElseIfExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#elseExpr.
    def enterElseExpr(self, ctx:KiwiParser.ElseExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#elseExpr.
    def exitElseExpr(self, ctx:KiwiParser.ElseExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#ternaryOperation.
    def enterTernaryOperation(self, ctx:KiwiParser.TernaryOperationContext):
        pass

    # Exit a parse tree produced by KiwiParser#ternaryOperation.
    def exitTernaryOperation(self, ctx:KiwiParser.TernaryOperationContext):
        pass


    # Enter a parse tree produced by KiwiParser#whileExpr.
    def enterWhileExpr(self, ctx:KiwiParser.WhileExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#whileExpr.
    def exitWhileExpr(self, ctx:KiwiParser.WhileExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#forExpr.
    def enterForExpr(self, ctx:KiwiParser.ForExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#forExpr.
    def exitForExpr(self, ctx:KiwiParser.ForExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#specialForExpr.
    def enterSpecialForExpr(self, ctx:KiwiParser.SpecialForExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#specialForExpr.
    def exitSpecialForExpr(self, ctx:KiwiParser.SpecialForExprContext):
        pass


    # Enter a parse tree produced by KiwiParser#display.
    def enterDisplay(self, ctx:KiwiParser.DisplayContext):
        pass

    # Exit a parse tree produced by KiwiParser#display.
    def exitDisplay(self, ctx:KiwiParser.DisplayContext):
        pass


    # Enter a parse tree produced by KiwiParser#function.
    def enterFunction(self, ctx:KiwiParser.FunctionContext):
        pass

    # Exit a parse tree produced by KiwiParser#function.
    def exitFunction(self, ctx:KiwiParser.FunctionContext):
        pass


    # Enter a parse tree produced by KiwiParser#functionParams.
    def enterFunctionParams(self, ctx:KiwiParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by KiwiParser#functionParams.
    def exitFunctionParams(self, ctx:KiwiParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by KiwiParser#params.
    def enterParams(self, ctx:KiwiParser.ParamsContext):
        pass

    # Exit a parse tree produced by KiwiParser#params.
    def exitParams(self, ctx:KiwiParser.ParamsContext):
        pass


    # Enter a parse tree produced by KiwiParser#give.
    def enterGive(self, ctx:KiwiParser.GiveContext):
        pass

    # Exit a parse tree produced by KiwiParser#give.
    def exitGive(self, ctx:KiwiParser.GiveContext):
        pass


    # Enter a parse tree produced by KiwiParser#functionCall.
    def enterFunctionCall(self, ctx:KiwiParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by KiwiParser#functionCall.
    def exitFunctionCall(self, ctx:KiwiParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by KiwiParser#stringExpr.
    def enterStringExpr(self, ctx:KiwiParser.StringExprContext):
        pass

    # Exit a parse tree produced by KiwiParser#stringExpr.
    def exitStringExpr(self, ctx:KiwiParser.StringExprContext):
        pass



del KiwiParser