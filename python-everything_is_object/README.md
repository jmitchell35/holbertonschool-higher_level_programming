## Resources

**Read or watch**:

*   [9.10. Objects and values](/rltoken/vu0q2rKj3XKGyDoqvx72sA "9.10. Objects and values")
*   [9.11. Aliasing](/rltoken/MOP1Saf_C2E_eHxKnZggHw "9.11. Aliasing")
*   [Immutable vs mutable types](/rltoken/vvV3pDEliqja6aAI7XFNiA "Immutable vs mutable types")
*   [Mutation](/rltoken/Xy3ZTgiwzUL_pLlB2rZoJw "Mutation") (_Only this chapter_)
*   [9.12. Cloning lists](/rltoken/2tqD3FclxPgvlTC70KQApw "9.12. Cloning lists")
*   [Python tuples: immutable but potentially changing](/rltoken/cEGMM3oDORTvSOgUi7Qnhg "Python tuples: immutable but potentially changing")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/SYBqBafJ9K7-vindoYatpA "explain to anyone"), **without the help of Google**:

### General

*   What is an object
*   What is the difference between a class and an object or instance
*   What is the difference between immutable object and mutable object
*   What is a reference
*   What is an assignment
*   What is an alias
*   How to know if two variables are identical
*   How to know if two variables are linked to the same object
*   How to display the variable identifier (which is the memory address in the CPython implementation)
*   What is mutable and immutable
*   What are the built-in mutable types
*   What are the built-in immutable types
*   How does Python pass variables to functions

## Requirements

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

### `.txt` Answer Files

*   Only one line
*   No Shebang on the first line (i.e. “#!/usr/bin/python3”)
*   All your files should end with a new line

## Tasks

### 1.

What function would you use to print the type of an object?

Write the name of the function in the file, without `()`.

  

### 2.

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

  

### 3.

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
\>>> a = 89
>>> b = 100
```
  

### 4.

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
\>>> a = 89
>>> b = 89
```
  

### 5.

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
\>>> a = 89
>>> b = a
```
  

### 6.

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
\>>> a = 89
>>> b = a + 1
```
  

### 7.

What do these 3 lines print?
```
\>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
  

### 8.

What do these 3 lines print?
```
\>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
  

### 9.

What do these 3 lines print?
```
\>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
  

### 10.

What do these 3 lines print?
```
\>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
  

### 11.

What do these 3 lines print?
```
\>>> l1 = \[1, 2, 3\]
>>> l2 = \[1, 2, 3\] 
>>> print(l1 == l2)
```
  

### 12.

What do these 3 lines print?
```
\>>> l1 = \[1, 2, 3\]
>>> l2 = \[1, 2, 3\] 
>>> print(l1 is l2)
```
  

### 13.

What do these 3 lines print?
```
\>>> l1 = \[1, 2, 3\]
>>> l2 = l1
>>> print(l1 == l2)
```
  

### 14.

What do these 3 lines print?
```
\>>> l1 = \[1, 2, 3\]
>>> l2 = l1
>>> print(l1 is l2)
```
  

### 15.

What does this script print?
```
l1 = \[1, 2, 3\]
l2 = l1
l1.append(4)
print(l2)
```
  

### 16.

What does this script print?
```
l1 = \[1, 2, 3\]
l2 = l1
l1 = l1 + \[4\]
print(l2)
```
  

### 17.

What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
  

### 18.

What does this script print?
```
def increment(n):
    n.append(4)

l = \[1, 2, 3\]
increment(l)
print(l)
```
  

### 19.

What does this script print?
```
def assign\_value(n, v):
    n = v

l1 = \[1, 2, 3\]
l2 = \[4, 5, 6\]
assign\_value(l1, l2)
print(l1)
```
  

### 20.

Write a function `def copy_list(a_list):` that returns a **copy** of a list.

*   The input list can contain any type of objects
*   Your file should be maximum 3-line long (no documentation needed)
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 19-main.py
#!/usr/bin/python3
copy\_list = \_\_import\_\_('19-copy\_list').copy\_list

my\_list = \[1, 2, 3\]
print(my\_list)

new\_list = copy\_list(my\_list)

print(my\_list)
print(new\_list)

print(new\_list == my\_list)
print(new\_list is my\_list)

guillaume@ubuntu:~/$ ./19-main.py
\[1, 2, 3\]
\[1, 2, 3\]
\[1, 2, 3\]
True
False
guillaume@ubuntu:~/$ wc -l 19-copy\_list.py 
3 19-copy\_list.py
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 21.
```
a = ()
```
Is `a` a tuple? Answer with `Yes` or `No`.

  

### 22.
```
a = (1, 2)
```
Is `a` a tuple? Answer with `Yes` or `No`.

  

### 23.
```
a = (1)
```
Is `a` a tuple? Answer with `Yes` or `No`.

  

### 24.
```
a = (1, )
```
Is `a` a tuple? Answer with `Yes` or `No`.

  

### 25.

What does this script print?
```
a = (1)
b = (1)
a is b
```
  

### 26.

What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
  

### 27.

What does this script print?
```
a = ()
b = ()
a is b
```
  

### 28.
```
\>>> id(a)
139926795932424
>>> a
\[1, 2, 3, 4\]
>>> a = a + \[5\]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

  

### 29.
```
\>>> a
\[1, 2, 3\]
>>> id (a)
139926795932424
>>> a += \[4\]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

  

### 30.

Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

*   introduction
*   id and type
*   mutable objects
*   immutable objects
*   why does it matter and how differently does Python treat mutable and immutable objects
*   how arguments are passed to functions and what does that imply for mutable and immutable objects

_If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post._

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
