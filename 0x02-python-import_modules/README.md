# 0x02. Python - import & modules

## Table Of Contents

### modules

- [0-add](#0-add)
- [1-calculation](#1-calculation)
- [2-args](#2-args)
- [3-infinite_add](#3-infinite_add)
- [4-hidden_discovery](#4-hidden_discovery)
- [5-variable_load](#5-variable_load)

## 0-add.py
Wrote the program that imports the function ****def add(a, b):** from the file ****add_0.py** 
and prints the result of the addition **1 + 2 = 3**

- the value 1 is assigned to variable a
- the value 2 is assigned to variable b
- Program prints: 

``` shell
1 + 2 = 3
```

- Code will not execute if imported with **\*** or dynamically using __import__

## 1-calculation

This program imports functions from the file **calculator_1.py**, does some Maths, and prints the result.

``` shell
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

- the value 10 to a variable a
- the value 5 to a variable b

## 2-args

Wrote a program that prints the number of and the list of its arguments.

### The output should be:

- Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
- **\:** (or **\.** if no arguments were passed) followed by
- a new line, followed by (if at least one argument),
- one line per argument:
- 
- the position of the argument (starting at 1) followed by **\:**, followed by the argument value and a new line
- The code is not executed when imported

## 3-infinite_add

The program prints the result of the addition of all arguments

- The output should be the result of the addition of all arguments, followed by a new line
- The code is not executed when imported

## 4-hidden_discovery

The program prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

### The output should be:

- Prints one name per line, in alpha order
- It only prints names that does not start with **__**
- The code is not be executed when imported

## 5-variable_load

Wrote the program that imports the variable a from the file variable_load_5.py and prints its value.

- The code will not be executed when imported
