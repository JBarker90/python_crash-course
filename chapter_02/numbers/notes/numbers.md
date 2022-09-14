## Numbers

1. Integers:

- You can add `(+)`, substract `(-)`, multiply `(*)`, and divide `(/)` integers in Python

```
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
>>> 3 * (2 + 4)
18
>>> 2 + 3*4
14
```

NOTE: Python does use the Order of Operations

- Python uses two multiplication symbols to represent exponents:

```
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

2. Floats:

- Python calls any number with a decimal point a *float*. This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number.

- Simply enter the numbers you want to use, and Python will most likely do what you expect:

```
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

3. Integers and Floats:

- When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float:

```
>>> 4/2
2.0
```

- If you mix an integer and a float in any other operation, you'll get a float as well:

```
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

4. Underscores in Numbers:

- When you're writing long numbers, you can group digits using underscores to make large numbers more readable. I created a new file called `underscore.py` for a proof of concept:

```
# When you print a number that was defined using underscores, Python prints only the digits

universe_age = 14_000_000_000
print(universe_age)
```

Ouput when run:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/numbers$ python3 underscore.py 
14000000000
```

5. Multiple Assignment:

- You can assign values to more than one variable using just a single line. This can help shorten your programs and make them easier to read; you'll use this technique most often when initializing a set of numbers.

- I created a file called `multiple.py`. Here's how you can initialize the variables x, y, and z to zero:

```
x, y, z = 0, 0, 0

print(x, y)
```

Output when run:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/numbers$ python3 multiple.py 
0 0
```

6. Constants:

- A *contstant* is like a variable whose value stays the same throughout the life of a program. Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed. This is in a file called `constants.py`:

```
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/numbers$ python3 constants.py 
5000
```