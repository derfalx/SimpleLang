grammar SimpleLang;

code : (statement | expr)+ ;

expr : arithmetic_expr SEMICOLON
     | bool_expr SEMICOLON
     | other_expr SEMICOLON
     ;

arithmetic_expr : LP arithmetic_expr RP
                | laexpr=arithmetic_expr op=(MUL | DIV) raexprl=arithmetic_expr
                | laexpr=arithmetic_expr op=(ADD | SUB) raexpr=arithmetic_expr
                | NUMBER
                | FLOAT
                | ID
                ;

bool_expr : LP bool_expr RP
          | lbexpr=bool_expr AND rbexpr=bool_expr
          | lbexpr=bool_expr OR rbexpr=bool_expr
          | NOT bool_expr
          | laexpr=arithmetic_expr EQUALS raexpr=arithmetic_expr
          | laexpr=arithmetic_expr op=(LESS_EQ_THAN | LESS_THAN) raexpr=arithmetic_expr
          | laexpr=arithmetic_expr op=(GREATER_EQ_THAN | GREATER_THAN) raexpr=arithmetic_expr
          | (TRUE | FALSE)
          | ID
          ;

other_expr : STR
            ;

statement : PRINT expr SEMICOLON
          | LET id=ID COLON type=(T_BOOL | T_FLOAT | T_NUMBER) ASSIGN val=expr SEMICOLON
          | id=ID ASSIGN aexpr=arithmetic_expr
          | id=ID ASSIGN bexpr=bool_expr
          ;

STR : '".*?"' ;
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
LP : '(' ;
RP : ')' ;
AND : 'and' ;
OR : 'or' ;
NOT : 'not' | '!';
EQUALS : '==' ;
TRUE : 'true' ;
FALSE : 'false' ;
LESS_THAN : '<' ;
LESS_EQ_THAN : '<=' ;
GREATER_THAN : '>' ;
GREATER_EQ_THAN : '>=' ;
ASSIGN : '=' ;
ID : [a-z]+ ;
SEMICOLON : ';' ;
COLON : ':' ;
fragment DIGIT : [0-9] ;
NUMBER : ('-'|'+')?DIGIT+ ;
FLOAT : ('-'|'+')?DIGIT+'.'DIGIT+ ;

PRINT : 'print' ;
LET : 'let';

T_BOOL : 'bool' ;
T_NUMBER : 'number' ;
T_FLOAT : 'float' ;
T_STRING : 'string' ;

WS : [ \t\r\n]+ -> skip ;

