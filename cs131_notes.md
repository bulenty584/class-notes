# Lecture 1, September 30, 2024

## Refresher

- Pass by value 
  - Formal parameter is a copy of the original variable
- Pass by reference
  - Formal parameter refers directly to the original variable
- Pass by pointer
  - Formal parameter is a pointer that contains the address of the original variable
  - The pointer parameter in the function generates a new pointer that points to the address passed into the function
  
## What is needed to specify details of a language

- Syntax spec (set of instructions to define what's legal or not in terms of syntax)
- Semantic Spec (how the syntax behaves: type checking, operator behavior, etc.)

## Compiler vs Linker

- *Compiler* is a program that translates program source into object modules (either machine language, or bytecode targeted at an interpreter)
  - Linker takes all files compiled (foo.o) and links them with other libraries to create final executable
- *Linker* is a program that combines mutiple object modules and libraries into a single executable file or library

## How does a compiler work

- Source file is fed into *Lexical analyzer* (converted to lexical units) which is fed into Parser (uses language grammar to make sure tokens are valid syntax
- *Parser* converts tokens into an abstract syntax tree
- *Semantic analyzer* checks types, behavior of everything and produces an annotated parse tree
- *Intermediate representation generator* either produces a different type of tree or generic Assembly language
- *Code generator* takes the previous tree or Assembly and converts it to byte code (your object files)

## What is an Interpreter

- A program that directly executes program statments without needing them to be compiled first into machine code

### How it works
- Load source file into RAM --> Initialize Data structures needed by interpreter --> We check if program finished running?
- If yes, we exit 
- If no, we fetch next statement to run, and repeat process


# Lecture 2, October 2, 2024

Interpreter takes source code, does some intermediate processing and runs instruction there and then and keeps moving on

## Python Lecture

### Allocation of Objects

In Python, all objects are references: When we assign objects and variables, python will create a new variable on the heap and the garbage collector cleans it up

### Class Variables

Class variables are static, any variable defined in a class, not as self, will be global and shared across all instances

### Copying Objects

Python has deep copying (makes a copy of the top-level object and every object referred to directly or indirectly by the top-level object)

Python also has shallow copying (makes a copy of only the top-level object)

### Object References

Assignments of object references do not make deep copies

### How are Lists implemented in Python??

As an array! O(n) to search a list, O(1) for retrieval, O(m+n) for appending one list to another (each index has a pointer to the element)


f :: ([Int] -> [String] -> a) -> a

