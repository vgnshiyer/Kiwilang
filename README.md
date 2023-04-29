# SER502-Spring23-Team5

##### Team members
1. Naga Venkata Dharani Vishwanadh Chinta
2. Sri Harsha Gajavalli
3. Vignesh Venkatachalam Iyer
4. Vamsi Krishna Yadav Loya
5. Anish Unnikrishnan Nair

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

**Link to Youtube Video**

Click here: https://youtu.be/8BzWCBAFuTo

**Note**
- We have implemented function declaration, function call for the language
    - Recursive functions are not working as of now in the current version. Any recursive function that you write will return a Null object.
- The grammar in the actual project may not be exactly equal to the grammar specified in milestone 1. 
    - We made some concious decisions with changing the grammar for the language as it felt feasible while implementing
    - However, the main objective of having a simple minimalistic language still holds true.
- This language does not have a compiler and a runtime. It is an interpreted language.