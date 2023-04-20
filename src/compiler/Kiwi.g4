/*
Version: 1
Date: April 19 2023
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
        : (declaration|ifExpr|whileExpr|forExpr|specialForExpr|display)
        ;

declaration
        : 'int' ID (ASSIGN arithmeticExpr)?
        | 'bool' ID (ASSIGN booleanExpr)?
        | ID ASSIGN arithmeticExpr 
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
        | SUB? DIGIT
        | SUB? ID
        ;

booleanExpr
        : booleanExpr operator=(EQ|NEQ) booleanExpr
        | booleanExpr operator=(AND|OR) booleanExpr
        | arithmeticExpr operator=(GT|LT|GTE|LTE|EQ|NEQ) arithmeticExpr
        | '(' booleanExpr ')'
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
        : 'print' (DIGIT|BOOL|ID|arithmeticExpr|booleanExpr)
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