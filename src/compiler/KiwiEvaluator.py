'''
Author: Vignesh Iyer
Version: 1
Date: April 20th 2023
'''

# reference: https://jason.whitehorn.us/blog/2021/02/08/getting-started-with-antlr-for-python/
import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.InputStream import InputStream
from lexer_and_parser.KiwiLexer import KiwiLexer
from lexer_and_parser.KiwiParser import KiwiParser
from lexer_and_parser.KiwiListener import KiwiListener

DEBUG_LEVEL = True

def prepare():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    filename = sys.argv[1]
    lexer = KiwiLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = KiwiParser(tokens, filename)
    tree = parser.program()
    if DEBUG_LEVEL:
        print(Trees.toStringTree(tree, None, parser))

    # visitor.eval(tree)

if __name__ == '__main__':
    prepare()