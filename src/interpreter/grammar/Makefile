antlr:
	sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar && \
	export CLASSPATH=".:antlr-4.9.2-complete.jar:$(CLASSPATH)" && \
	pip3 install antlr4-python3-runtime==4.9.2 && \
	java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 Kiwi.g4 -visitor -o ../lexer_and_parser