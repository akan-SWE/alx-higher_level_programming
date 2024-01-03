# 0x06. Python - Classes and Objects in Python

This repository contains a collection of Python files focusing on Object-Oriented Programming (OOP), each demonstrating different implementations of classes and objects.

## Table of Contents

Modules:

- [0-square](#0-square)
- [1-square](#1-square)
- [2-square](#2-square)
- [3-square](#3-square)
- [4-square](#4-square)
- [5-square](#5-square)
- [6-square](#6-square)

## 0-square

An empty class, **Square**, is defined to represent a square.

## 1-square

- The **Square** class (built upon **0-square**) is defined.
- It includes a private instance attribute, **size**, allowing instantiation with a provided **size** (without type/value verification).

## 2-square

Building on **1-square**, the **Square** class is further developed to:

- Include a private instance attribute, **size**.
- Enable instantiation with an optional **size: def __init__(self, size=0)**:
  - If the provided **size** is not an integer, it raises a TypeError with the message **"size must be an integer"**.
  - If the **size** is less than 0, it raises a ValueError with the message **"size must be >= 0"**.

## 3-square

Based on **2-square**, the **Square** class is enhanced to:

- Feature a private instance attribute, **size**.
- Allow instantiation with an optional **size: def __init__(self, size=0):**
  - If **size** isn't an integer, it raises a TypeError with the message **"size must be an integer"**.
  - If **size** is less than 0, it raises a ValueError with the message **"size must be >= 0"**.
- Introduce a public instance method, **def area(self):**, returning the current square area.

## 4-square

Extending from **3-square**, this iteration of the **Square** class includes:

- A private instance attribute, **size**.
  - A property **def size(self):** to retrieve the size.
  - A property setter **def size(self, value):** to set the size:
    - Verifies that the **size** is an integer; otherwise, it raises a TypeError with the message **"size must be an integer"**.
    - Ensures that the **size** is not less than 0; otherwise, it raises a ValueError with the message **"size must be >= 0"**.
- Instantiation with an optional **size: def __init__(self, size=0):**
- A public instance method, **def area(self):**, which returns the current square area.

## 5-square

Building upon **4-square**, this version of the **Square** class introduces:

- A private instance attribute, **size**.
  - A property **def size(self):** to retrieve the size.
  - A property setter **def size(self, value):** to set the size:
    - Validates that the **size** is an integer; otherwise, raises a TypeError with the message **"size must be an integer"**.
    - Ensures that the **size** is not less than 0; otherwise, raises a ValueError with the message **"size must be >= 0"**.
- Instantiation with an optional **size: def __init__(self, size=0):**
- Public instance methods:
  - **def area(self):** returns the current square area.
  - **def my_print(self):** prints the square with the character #.

## 6-square

Based on **5-square**, the **Square** class is expanded to include:

- A private instance attribute, **size**:
  - A property **def size(self):** to retrieve the size.
  - A property setter **def size(self, value):** to set the size:
    - Ensures that the **size** is an integer; otherwise, raises a TypeError with the message **"size must be an integer"**.
    - Verifies that the **size** is not less than 0; otherwise, raises a ValueError with the message **"size must be >= 0"**.
- Another private instance attribute, **position**:
  - A property **def position(self):** to retrieve the position.
  - A property setter **def position(self, value):** to set the position:
    - Validates that the **position** is a tuple of 2 positive integers; otherwise, raises a TypeError with the message **"position must be a tuple of 2 positive integers"**.
- Instantiation with optional **size** and **position: def __init__(self, size=0, position=(0, 0)):**
- Public instance methods:
  - **def area(self):** returns the current square area.
  - **def my_print(self):** prints the square with the character #.
    - If **size** is equal to 0, it prints an empty line.
    - Uses **position** by adding spaces; it won't fill lines by spaces when **position[1] > 0**.
