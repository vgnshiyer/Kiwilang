/*
Author: Vignesh Iyer
Version: 1
Last Updated: April 21 2023
*/

grammar Kiwi;

program
        : block
        ;

block 
        :
        | statement+
        ;

statement
        : (declaration|incrementExpr|condExpr|whileExpr|forExpr|specialForExpr|display|function|give|functionCall)
        ;

declaration
        : 'int' ID (ASSIGN arithmeticExpr)?
        | 'bool' ID (ASSIGN booleanExpr)?
        | 'str' ID (ASSIGN stringExpr)?
        | ID ASSIGN arithmeticExpr 
        | ID ASSIGN booleanExpr
        | ID ASSIGN stringExpr
        | ID ASSIGN ternaryOperation
        ;

incrementExpr
        : ID '++'
        | ID '--'
        | ID operator=(ADD|SUB|MUL|DIV) '=' arithmeticExpr
        ;

arithmeticExpr
        : arithmeticExpr operator=(MUL|DIV) arithmeticExpr
        | arithmeticExpr operator=(ADD|SUB) arithmeticExpr
        | '(' arithmeticExpr ')'
        | functionCall
        | SUB? DIGIT
        | SUB? ID
        ;

booleanExpr
        : booleanExpr operator=(EQ|NEQ) booleanExpr
        | booleanExpr operator=(AND|OR) booleanExpr
        | arithmeticExpr operator=(GT|LT|GTE|LTE|EQ|NEQ) arithmeticExpr
        | '(' booleanExpr ')'
        | functionCall
        | (NOT)? BOOL
        | (NOT)? ID
        ;

condExpr
        : ifExpr (elseIfExpr)* (elseExpr)?
        ;

ifExpr
        : 'if' booleanExpr '{' block '}'
        ;

elseIfExpr
        : 'else if' booleanExpr '{' block '}'
        ;

elseExpr
        : 'else' '{' block '}'
        ;

ternaryOperation
        : booleanExpr '?' (arithmeticExpr|booleanExpr) ':' (arithmeticExpr|booleanExpr)
        ;

whileExpr
        : 'while' booleanExpr '{' block '}'
        ;

forExpr
        : 'for' '(' declaration ';' booleanExpr ';' (declaration|incrementExpr) ')' '{' block '}'
        ;

specialForExpr
        : ('for' ID 'in' 'range' '(' DIGIT ')'|'for' ID 'in' 'range' '(' DIGIT ',' DIGIT ')') '{' block '}'
        ;

display
        : 'print' (DIGIT|BOOL|ID|arithmeticExpr|booleanExpr|STRING)
        ;

function
        : 'fn' ID ':' params '{' block '}'
        ;

params
        : '()'
        | '(' (arithmeticExpr|booleanExpr) (',' (arithmeticExpr|booleanExpr))* ')'
        ;

give
        : 'give' (ID|BOOL|STRING|arithmeticExpr|booleanExpr|functionCall)
        ;

functionCall
        : ID params
        ;

stringExpr
        : STRING
        ;

STRING
    : '"' (~'"' | '\n' | '\r' | '\\' . | ~('\\'|'"'))* '"'
    ;

DIGIT
        : [1-9] [0-9]*
        | '0'
        ;

BOOL
        : 'true'
        | 'false'
        ;

ADD     : '+';
SUB     : '-';
MUL     : '*';
DIV     : '/';

AND     : 'and';
OR      : 'or' ;
NOT     : 'not';
EQ      : '==';
NEQ     : '!=';
GT      : '>';
GTE     : '>=';
LT      : '<';
LTE     : '<=';
ASSIGN  : ':=';

ID
        : [a-zA-Z_] [a-zA-Z_0-9]*
        ;

WS      : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
Comment : ('//' ~[\r\n]* | '/*' .*? '*/') -> skip;