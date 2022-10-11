## Making Numerical Lists

1. Many reasons exist to store a set of numbers. 

- For example, you'll need to keep track of the positions of each character in a game, and you might want to keep track of a player's high scores as well. 

2. Using the `range()` Function:

- Python's `range()` function makes it easy to generate a series of numbers. 

- For example, you can use the `range()` function to print a series of numbers like in the `first_numbers.py` file:

```
for value in range(1, 5):
    print(value)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/numerical_lists$ python3 first_numbers.py
1
2
3
4
```

- Even though the range is 1 to 5, Python will only print out 1-4. This is another result of the off-by-one behavior often seen in programming languages. 

- The `range()` function causes Python to start counting at the first value you give it, and it stops whne it reaches the second value you provide. 

- To print the numbers from 1 to 5, you would use `range(1, 6)`

```
for value in range(1, 6):
    print(value)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/numerical_lists$ python3 first_numbers.py
1
2
3
4
5
```

3. Using `range()` to Make a List of Numbers:

- If you want to make a list of numbers, you can convert the results of `range()` directly into a list using the `list()` function.

- In the example in the previous section, we simply printed out a series of numbers. We can use `list()` to convert that same set of numbers into a list:

```
numbers = list(range(1, 6))
print(numbers)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/numerical_lists$ python3 numbers.py
[1, 2, 3, 4, 5]
```

- We can also use the `range()` function to tell Python to skip numbers in a given range. If you pass a third argument to `range()`, Python uses that value as a step size when generating numbers. 

- In `even_numbers.py`, this is how to list the even numbers between 1 and 10.

```
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/numerical_lists$ python3 even_numbers.py
[2, 4, 6, 8, 10]
```

- You can create almost any set of numbers you want by using the `range()` function. For example, consider how you might make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). 

NOTE: In Python, two asterisks `(**)` represent exponents. Here's how you might put the first 10 square numbers into a list in `squares.py`:

```
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/numerical_lists$ python3 squares.py
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

TIP: To write this code more concisely, omit the temporary variable `square` and append each new value directly to the list:

```
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
```

4. List Comprehensions:

- The approach described earlier for generating the list `squares` consisted of using three or four lines of code. 

- A *list comprehension* allow you to generate this same list in just one line of code. A list comprehension combines the `for` loop and the creation of new elements into one line, and automatically appends each new element. 

- The following example builds the same list of square numbers you saw earlier but uses a list comprehension:

```
squares = [value**2 for value in range(1, 11)]
print(squares)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/numerical_lists$ python3 squares.py
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```