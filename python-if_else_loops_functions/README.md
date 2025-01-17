Python - if/else, loops, functions
==================================

*   Novice
*   By: Guillaume
*   Weight: 1
*   Your score will be updated as you progress.

*   [Description](#description)
*   [Quiz](#quiz)

[Go to tasks](#)

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming\+/233/code.png)

Resources
---------

**Read or watch**:

*   [More Control Flow Tools](/rltoken/X77zAIll3ePP3gA-eUSiiA "More Control Flow Tools") (_Read until “4.6. Defining Functions” included_)
*   [IndentationError](/rltoken/2JgLsB5c9CpN5xkYS9wMKQ "IndentationError")
*   [How To Use String Formatters in Python 3](/rltoken/Bt4ISTvUyfB6lFxEoL3NwQ "How To Use String Formatters in Python 3")
*   [Learn to Program 2 : Looping](/rltoken/qwVdwqW4LROXY0CIbWNiAw "Learn to Program 2 : Looping")
*   [Pycodestyle – Style Guide for Python Code](/rltoken/8D5JdrayXbe3ZzPWr335dQ "Pycodestyle -- Style Guide for Python Code")

**man or help**:

*   `python3`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/cpnHPq4-L7SEER4Skw0Cbw "explain to anyone"), **without the help of Google**:

### General

*   Why indentation is so important in Python
*   How to use the `if`, `if ... else` statements
*   How to use comments
*   How to affect values to variables
*   How to use the `while` and `for` loops
*   How to use the `break` and `continues` statements
*   How to use `else` clauses on loops
*   What does the `pass` statement do, and when to use it
*   How to use `range`
*   What is a function and how do you use functions
*   What does return a function that does not use any `return` statement
*   Scope of variables
*   What’s a traceback
*   What are the arithmetic operators and how to use them

Requirements
------------

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.\*)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

More Info
---------

_Note_: you do not need to understand lists yet.

**Great!** You've completed the quiz successfully! Keep going! (Hide quiz)

Tasks
-----

### 0\. Positive anything is better than negative nothing

mandatory

Score: 100.00% (Checks completed: 100.00%)

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

*   You can find the source code [here](/rltoken/aBRwd0uo_aZMPK2CBG1syg "here")
*   The variable `number` will store a different value every time you will run this program
*   You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
*   The output of the program should be:
    *   The number, followed by
        *   if the number is greater than 0: `is positive`
        *   if the number is 0: `is zero`
        *   if the number is less than 0: `is negative`
    *   followed by a new line

    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    -4 is negative
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    0 is zero
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    -3 is negative
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    -10 is negative
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    10 is positive
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    -5 is negative
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    6 is positive
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    7 is positive
    guillaume@ubuntu:\~/$ ./0-positive_or_negative.py 
    5 is positive
    guillaume@ubuntu:\~/$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-if_else_loops_functions`
*   File: `0-positive_or_negative.py`

### 1\. The last digit

mandatory

Score: 100.00% (Checks completed: 100.00%)

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

*   You can find the source code [here](/rltoken/UdohgX1ToNOVf4cAa3KJxA "here")
*   The variable `number` will store a different value every time you will run this program
*   You don’t have to understand what `import`, `random.randint` do. **Please do not touch this code**. This line should not change: `number = random.randint(-10000, 10000)`
*   The output of the program should be:
    *   The string `Last digit of`, followed by
    *   the number, followed by
    *   the string `is`, followed by the last digit of `number`, followed by
        *   if the last digit is greater than 5: the string `and is greater than 5`
        *   if the last digit is 0: the string `and is 0`
        *   if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
    *   followed by a new line

    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of 4205 is 5 and is less than 6 and not 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of -626 is -6 and is less than 6 and not 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of 1144 is 4 and is less than 6 and not 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of -9200 is 0 and is 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of 5247 is 7 and is greater than 5
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of -9318 is -8 and is less than 6 and not 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of 3369 is 9 and is greater than 5
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of -5224 is -4 and is less than 6 and not 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of -4485 is -5 and is less than 6 and not 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of 3850 is 0 and is 0
    guillaume@ubuntu:\~/$ ./1-last_digit.py
    Last digit of 5169 is 9 and is greater than 5
    guillaume@ubuntu:\~/$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-if_else_loops_functions`
*   File: `1-last_digit.py`

### 2\. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

*   Use only one `print` function with string format
*   Use only one loop in your code
*   You are not allowed to store characters in a variable
*   You are not allowed to import any module

    guillaume@ubuntu:\~/$ ./2-print_alphabet.py
    abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:\~/$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-if_else_loops_functions`
*   File: `2-print_alphabet.py`

### 3\. When I was having that alphabet soup, I never thought that it would pay off

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a program that prints the ASCII alphabet, in lowercase, reversed (from `z` to `a`), not followed by a new line.

*   Use only one `print` function with string format
*   Use only one loop in your code
*   You are not allowed to store characters in a variable
*   You are not allowed to import any module

    guillaume@ubuntu:\~/$ ./3-print_alphabt_reversed.py
    zyxwvutsrqponmlkjihgfedcba
    guillaume@ubuntu:\~/$ 
    
**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-if_else_loops_functions`
*   File: `3-print_alphabet_reversed.py`

### 4\. Hexadecimal printing

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a program that prints all the numbers from `0` to `98` in decimal and in hexadecimal (lowercase), separated by a space.

*   You can use `hex()` to print the hexadecimal representation of a number
*   You are not allowed to import any module

    guillaume@ubuntu:\~/$ ./4-print_hexadecimal.py
    0 0x0
    1 0x1
    2 0x2
    3 0x3
    4 0x4
    5 0x5
    6 0x6
    7 0x7
    8 0x8
    9 0x9
    10 0xa
    11 0xb
    12 0xc
    13 0xd
    14 0xe
    15 0xf
    16 0x10
    17 0x11
    18 0x12
    19 0x13
    20 0x14
    21 0x15
    22 0x16
    23 0x17
    24 0x18
    25 0x19
    26 0x1a
    27 0x1b
    28 0x1c
    29 0x1d
    30 0x1e
    31 0x1f
    32 0x20
    33 0x21
    34 0x22
    35 0x23
    36 0x24
    37 0x25
    38 0x26
    39 0x27
    40 0x28
    41 0x29
    42 0x2a
    43 0x2b
    44 0x2c
    45 0x2d
    46 0x2e
    47 0x2f
    48 0x30
    49 0x31
    50 0x32
    51 0x33
    52 0x34
    53 0x35
    54 0x36
    55 0x37
    56 0x38
    57 0x39
    58 0x3a
    59 0x3b
    60 0x3c
    61 0x3d
    62 0x3e
    63 0x3f
    64 0x40
    65 0x41
    66 0x42
    67 0x43
    68 0x44
    69 0x45
    70 0x46
    71 0x47
    72 0x48
    73 0x49
    74 0x4a
    75 0x4b
    76 0x4c
    77 0x4d
    78 0x4e
    79 0x4f
    80 0x50
    81 0x51
    82 0x52
    83 0x53
    84 0x54
    85 0x55
    86 0x56
    87 0x57
    88 0x58
    89 0x59
    90 0x5a
    91 0x5b
    92 0x5c
    93 0x5d
    94 0x5e
    95 0x5f
    96 0x60
    97 0x61
    98 0x62
    guillaume@ubuntu:\~/$ 

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-if_else_loops_functions`
*   File: `4-print_hexadecimal.py`
