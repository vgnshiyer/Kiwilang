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
        : (declaration|ifExpr|whileExpr|forExpr|specialForExpr|display|function|give|functionCall)
        ;

declaration
        : 'int' ID (ASSIGN arithmeticExpr)?
        | 'bool' ID (ASSIGN booleanExpr)?
        | 'str' ID (ASSIGN STRING)?
        | ID ASSIGN arithmeticExpr 
        | ID ASSIGN booleanExpr
        | ID ASSIGN stringExpr
        ;

incrementExpr
        : ID ASSIGN arithmeticExpr
        | ID ASSIGN booleanExpr
        | ID '++'
        | ID '--'
        | ID operator=(ADD|SUB|MUL|DIV) ASSIGN arithmeticExpr
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

ifExpr
        : 'if' booleanExpr '{' block '}' (elseIfExpr)* ('else' '{' block '}')?
        ;

elseIfExpr
        : 'else if' booleanExpr '{' block '}'
        ;

whileExpr
        : 'while' booleanExpr '{' block '}'
        ;

forExpr
        : 'for' '(' declaration ';' booleanExpr ';' incrementExpr ')'
        ;

specialForExpr
        : ('for' ID 'in' 'range' '(' DIGIT ')'|'for' ID 'in' 'range' '(' DIGIT ',' DIGIT ')')
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