# Kiwi Language

Kiwi is an imperative programming language that follows a minimalistic design for writing simple programs.
The name given to the language emphasizes the simplicity and ease of use of the language.
It has a syntax that is easy to learn, with familiar constructs for control flow, variables and functions found in most modern programming languages.
Kiwi also includes a number of built-in data types(numbers, booleans, strings), logic operators(AND, OR, NOT). Additionally, it also supports the ternary operator.

Language Grammar:
Program Structure: A program is composed of a series of functions and a main block containing declarations and commands.

Blocks: A block consists of a series of function definitions followed by a series of declarations and commands. Function definitions are optional and can be omitted if not required.

Declarations: Variables can be declared with a specific data type (let, int, float, or string) and an optional initial value. Ternary expressions can also be used as initial values.

Commands: The language supports various commands, including:

Print command for outputting expressions.
Variable assignment using expressions or ternary expressions.
Conditional statements (if-else) with Boolean expressions.
While loops with a Boolean condition.
For loops with two forms: traditional counter-based loops and range-based loops.
Functions: Functions are defined with a name, input parameters, a block of declarations and commands, and a return statement using the "give" keyword.

Boolean Expressions: Booleans can be represented by true, false, equality comparisons between expressions, or negated Boolean expressions.

Expressions: Expressions can be formed using basic arithmetic operations (addition, subtraction, multiplication, division), parentheses for grouping, variables, or numbers.

Ternary Expressions: The language supports ternary expressions in the form "Identifier == Expression ? Expression : Expression".

Data Types: The language supports four data types: let (for type inference), int, float, and string.

Identifiers: Identifiers are used for naming variables and functions and must begin with a letter or underscore, followed by any combination of letters, digits, or underscores.

Numbers: Numbers are sequences of digits.

Comparisons: Comparison operators include less than, greater than, less than or equal to, greater than or equal to, and equality.

This grammar defines a versatile imperative programming language with support for modern programming constructs such as functions, loops, and conditional statements.

Checkout: /src/interpreter/grammar/Kiwi.g4

**Program to check if a number is a prime number**

```
fn isprime : (n) {
    bool fl := true
    for(int i:=2;i<n;i++){
        if(i*(n/i)==n){
            fl := false
        }
    }
    print n
    if(fl==false){
        print " is not a prime number."
    }else{
        print " is a prime number."
    }
}

isprime(17)
```

**OS/Platform**
```
MacOs
Windows 
Linux
```

**The requirements are :**

    1. Python version 3.7 or higher
    2. ANTLR4

**Directions to install**

*Install requirements*
```
pip3 install -r requirements.txt
```
Note: Use pip if you do not have pip3 in your path

**Directions to build/run**

*Set alias for kiwi language*
```
alias kiwi='python3 ./src/interpreter/KiwiEvaluator.py'
```

**One line command**

*Run a kiwi file*
```
kiwi data/helloworld.kiwi
```

**Note**

If alias does not work on your system, run
```
python3 ./src/interpreter/KiwiEvaluator.py <filename>.kiwi
```

