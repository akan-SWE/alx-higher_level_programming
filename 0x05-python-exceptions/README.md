# 0x05. Python - Exceptions 

## Python Project files (.py)

- [0-safe_print_list](#0-safe_print_list)
- [1-safe_print_integer](#1-safe_print_integer-)
- [2-safe_print_list_integers](#2-safe_print_list_integers)
- [3-safe_print_division](#3-safe_print_division)
- [4-list_divisioin](#4-list_division)
- [5-raise_exception](#5-raise_exception)
- [6-raise_exception_msg](#6-raise_exception_msg)


## 0-safe_print_list

Wrote the function that prints x elements of a list.

**Prototype: def safe\_print\_list(my\_list=[], x=0):**

- **my_list** can contain any type (integer, string, etc.)
- All elements are printed on the same line
- x represents the number of elements to print
- x can be bigger than the length of **my_list**
- Returns the real number of elements printed

## 1-safe_print_integer 

The function prints an integer with **"{:d}".format().**

**Prototype: def safe\_print\_integer(value):**
- value can be any type (integer, string, etc.)
- Returns **True** if **value** has been correctly printed (it means the value is an integer)
- Otherwise, returns False 

## 2-safe_print_list_integers

The function prints the first x elements of a list and only integers.

**Prototype: def safe_print_list_integers(my_list=[], x=0):**

- **my_list** can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed

The function divides 2 integers and prints the result.

## 3-safe_print_division

**Prototype: def safe\_print\_division(a, b):**

- You can assume that a and b are integers
- The result of the division should print on the **finally**: section preceded by Inside result:
- Returns the value of the division, otherwise: None

## 4-list_division

The function divides element by element 2 lists.

**Prototype: def list_division(my_list_1, my_list_2, list_length):**

- **my_list_1 and **my_list_2** can contain any type (integer, string, etc.)
- list_length can be bigger than the length of both lists
- Returns a new list (length = list_length) with all divisions
- If 2 elements can’t be divided, the division result should be equal to 0
- If an element is not an integer or float:
    - print: **wrong type**
- If the division can’t be done **(/0)**:
    - print: **division by 0**
- If **my_list_1** or **my_list_2** is too short
    - print: **out of range**


## 5-raise_exception

The function raises a type exception.

**Prototype: def raise\_exception():**

 
## 6-raise_exception_msg

Wrote function that raises a name exception with a message.

**Prototype: def raise\_exception\_msg(message=""):**

