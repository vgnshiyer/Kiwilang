grammar kiwi_grammar;

program
        : block
        ;

block 
        :
        | statement+
        ;

statement
        : (ifExpr|whileExpr|forExpr|declaration)
        ;

declaration
        : 'int' ID (ASSIGN arithmeticExpr)?
        | 'bool' ID (ASSIGN booleanExpr)?
        | 'str' ID (ASSIGN STRING)?
        | ID ASSIGN arithmeticExpr
        | ID ASSIGN booleanExpr
        | ID ASSIGN STRING
        ;

arithmeticExpr
        : arithmeticExpr operator=(MUL|DIV) arithmeticExpr
        | arithmeticExpr operator=(ADD|SUB) arithmeticExpr
        | '(' arithmeticExpr ')'
        | SUB? DIGIT
        | SUB? ID
        ;

booleanExpr
        : booleanExpr operator=(EQUALS|NOTEQUALS) booleanExpr
        | booleanExpr operator=(AND|OR) booleanExpr
        | 

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | '(' expr ')'                             # ParenExpr 
    | atom=HELLO                               # HelloExpr
    | atom=BYE                                 # ByeExpr
    ;

HELLO: ('hello'|'hi')  ;
BYE  : ('bye'| 'tata') ;
INT  : [0-9]+         ;
WS   : [ \t]+ -> skip ;