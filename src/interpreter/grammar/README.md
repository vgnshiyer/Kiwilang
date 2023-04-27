##### Before you begin

### Setup antlr

```
sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
export CLASSPATH=".:antlr-4.9.2-complete.jar:$CLASSPATH"
alias antlr4='java -jar antlr-4.9.2-complete.jar'
pip3 install antlr4-python-runtime==4.9.2
```

*Currently make antlr does not work. Manually copy each command and run on your terminal*

### Prepare lexer and parser for Kiwi.g4

```
antlr4 -Dlanguage=Python3 Kiwi.g4 -visitor -o ../lexer_and_parser
```

*Perform a run operation everytime you make changes to the grammar*

