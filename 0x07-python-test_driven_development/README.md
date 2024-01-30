# 0x07. Python - Test-driven development


# Table Of Contents

Modules

- [0-add_integer](#0-add_integer)
- [2-matrix_divided](#2-matrix_divided)
- [3-say_my_name](#3-say_my_name)
- [4-print_square](#4-print_square)
- [5-text_indentation](#5-text_indentation)
- [tests/6-max_integer_test](#6-max_integer_test)
- [100-matrix_mul](#100-matrix_mul)
- [101-lazy_matrix_mul](#101-lazy_matrix_mul)
 
## 0-add_integer

**def add_integers(a, b=98): adds two integers

- **a** and **b** must be integers or floats, otherwise raise a TypeError exception with the message **a must be an integer** or **b must be an integer**
- **a** and **b** must be first cast to integers if they are float
- Returns an integer: the addition of **a** and **b**

## 2-matrix_divided

**def matrix_divided(matrix, div):** Divides all elements of a matrix

- **matrix** must be a list of lists of integers or floats, otherwise it raises a **TypeError** with the message **matrix must be a matrix (list of lists) of integers/floats**
- Each row of the **matrix** must be of the same size, otherwise raise a **TypeError** exception with the message **Each row of the matrix must have the same size**
- **div** must be a number (integer or float), otherwise raise a **TypeError** exception with the message **div must be a number**
- **div** can’t be equal to 0, otherwise raise a **ZeroDivisionError** exception with the message **division by zero**
- All elements of the matrix is divided by div and rounded to 2 decimal places<br>
- Returns a new matrix

### doctest file 
    tests/2-matrix_divided.txt

## 3-say_my_name

**def say_my_name(first_name, last_name=""):** Prints My name is <**first name**> <**last name**>

- first_name and last_name must be strings otherwise, raises a **TypeError** exception with the message **first_name must be a string or last_name must be a string**

### doctest file
    tests/3-say_my_name.txt

## 4-print_square

**def print_square(size):** prints a square with the character **#**

- **size** is the size length of the square
- **size** must be an integer, otherwise raise a **TypeError** exception with the message
```
size must be an integer
```
- if **size** is less than 0, raise a **ValueError** exception with the message **size must be >= 0**
- if **size** is a float and is less than 0, raise a **TypeError** exception with the message **size must be an integer**
 
### doctest file
    tests/4-print_square.txt

## 5-text_indentation

**def text_indentation(text):** The function prints a text with 2 new lines after each of these characters: **., ? and :**

- text must be a string, otherwise raise a **TypeError** exception with the message **text must be a string**
- There is no space at the beginning or at the end of each printed line.

### doctest file
    tests/5-text_indentation.txt

## 6-max_integer_test

- A unit tests for the function **def max_integer(list=[]):** using the unittest module
- All edge cases has been covered

## 100-matrix_mul

**def matrix_mul(m_a, m_b):** The function that multiplies 2 matrices

**m_a** and **m_b** are validated with these requirements in this order

**m_a and m_b** must be an list of lists of integers or floats:

- if **m_a** or **m_b** is not a list: raise a **TypeError** exception with the message **m_a must be a list or m_b must be a list**
- if **m_a** or **m_b** is not a list of lists: raise a **TypeError** exception with the message **m_a must be a list of lists or m_b must be a list of lists**
- if **m_a** or **m_b** is empty (it means:= [] or = [[]]): raise a **ValueError** exception with the message **m_a can't be empty** or **m_b can't be empty**
- if one element of those list of lists is not an integer or a float: raise a **TypeError** exception with the message **m_a should contain only integers or floats** or **m_b should contain only integers or floats**
- if **m_a** or **m_b** is not a rectangle (all ‘rows’ should be of the same size): raise a **TypeError** exception with the message **each row of m_a must be of the same size or each row of m_b must be of the same size**
- If **m_a** and **m_b** can’t be multiplied: raise a **ValueError** exception with the message **m_a and m_b can't be multiplied**

### doctest file
    tests/100-matrix_mul.txt

## 101-lazy_matrix_mul
**def lazy_matrix_mul(m_a, m_b):** multiplies 2 matrices by using the module **NumPy**

To install it: 
```shell
pip3 install numpy==1.15.0
```
Test cases is the same as **100-matrix_mul** but with new exception **type/message**
### doctest file
    tests/101-lazy_matrix_mul.txt