grammar steer;

// Top-level rule
program: statement+ EOF;

// Statements
statement:
	varDeclaration
	| funcDefinition
	| forLoop
	| whileLoop
	| ifStatement
	| writeStatement
	| aiInstruction
	| functionCall
	| expression;

varDeclaration: IDENTIFIER '=' expression;
funcDefinition:
	'function' IDENTIFIER '(' paramList? ')' ':' statement+;
forLoop:
	'for' IDENTIFIER 'in' 'range' '(' expression ')' ':' statement+;
whileLoop: 'while' expression ':' statement+;
ifStatement:
	'if' expression ':' statement+ (
		'elif' expression ':' statement+
	)* ('else' ':' statement+)?;
writeStatement:
	'write' '(' (TEMPLATE_STRING | LITERAL | STRING_LITERAL) ')';
aiInstruction:
	'ai' '(' (TEMPLATE_STRING | LITERAL | STRING_LITERAL) ')';
functionCall: IDENTIFIER '(' paramList? ')';

paramList: IDENTIFIER (',' IDENTIFIER)*;

// Expressions
expression:
	expression OPERATOR expression
	| '(' expression ')'
	| functionCall
	| IDENTIFIER
	| BOOLEAN
	| LITERAL
	| extractFunc;

extractFunc:
	'extract' '(' expression ',' (
		TEMPLATE_STRING
		| LITERAL
		| STRING_LITERAL
	) ')';

// Lexer rules
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
BOOLEAN: 'True' | 'False';
LITERAL: [0-9]+ | '"' .*? '"';
TEMPLATE_STRING: '`' ('{' IDENTIFIER '}' | .)*? '`';
STRING_LITERAL: '\'' .*? '\'';
OPERATOR:
	[+\-*/%]
	| '=='
	| '!='
	| '<'
	| '<='
	| '>'
	| '>='
	| 'and'
	| 'or';

// Ignore whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '#' ~[\r\n]* -> skip;