# Conditional Tests

### 1. At the heart of every `if` statement is an expression that can be evaluated as `True` or `False` and is called a *conditional test*. 

### 2. Checking for Equality

- Most conditional tests compare the current value of a variable to a specific value of interest. 

- The simplest conditional test checks whether the value of a variable is equal to the value of interest:

```
>>> car = 'bmw'
>>> car == 'bmw'
True
```

- When the value of the car is anything other than `'bmw'` this test returns `False`

```
>>> print(car)
bmw
>>> car == 'audi'
False
>>> car == 'BMW'
False
```

### 3. Ignoring Case When Checking for Equality

- As pointed in the example above, testing for equality is case sensitive. Two values with different capitalization are not considered equal

```
>>> car = 'Audi'
>>> car == 'audi'
False
```

- You can convert the variables value to lowercase using the `lower()` method. This does not change the value that was originally stored in the variable, it just temporarily converts the variable to all lowercase.

```
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> print(car)
Audi
```

NOTE: You can do the same thing by using the `upper()` method.

```
>>> car = 'bmw'
>>> car == 'BMW'
False
>>> car.upper() == 'BMW'
True
>>> print(car)
bmw
```

### 4. Checking for Inequality

- When you want to determine whether two values are NOT equal, you can combine an exclamation point and an equal sign `(!=)`.

- The exclamation point represents *not* as it does in many programming languages. 

- Let's use another `if` statement to examine how to use the inequality operator. We'll store a requested pizza topping in a variable and then print a message if the person did not order anchovies in the `toppings.py` file.

```
requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_05/conditional_tests$ python3 toppings.py
Hold the anchovies!
```

### 5. Numerical Comparisons

- Testing numerical values is pretty straightforward. The following code checks whether a person is 18 years old.

```
>>> age = 18
>>> age == 18
True
```

- You can also test to see if two numbers are not equal. For example, the `magic_number.py` file prints a message if the given answer is not correct.

```
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_05/conditional_tests$ python3 magic_number.py
That is not the correct answer. Please try again!
```

- We can also refine this to force the user to guess a number. If the answer is equal to 42 it will print a message that says congratulations.

```
answer = int(input("I am thinking of a number between 1 and 100. What is it?\nYour answer: "))

if answer == 42:
    print("Congratulations! You guessed the answer!!!")
else:
    print("That is not the correct answer. Please try again!")
```

Output:

```
I am thinking of a number between 1 and 100. What is it?
Your answer: 2
That is not the correct answer. Please try again!

I am thinking of a number between 1 and 100. What is it?
Your answer: 42
Congratulations! You guessed the answer!!!
```

### 6. Using `and` to Check Multiple Conditions

- To check whether two conditions are bot `True` simultaneously, use the keyword `and` to combine the two conditional tests; if each test passes, the overall  expression evaluates to `True`.

- If either test failes or if both tests fail, the expression evaluates to `False`. 

```
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False

>>> age_0 >= 21 and age_1 <= 21
True
```

### 7. Using `or` to Check Multiple Conditions

- The keyword `or` allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass.

```
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True

>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 8. Checking Whether a Value Is in a List

- To find out whether a particular value is already in a list, use the keyword `in`. 
- This is in the `banned_users.py` file

```
banned_users = ['andrew', 'carolina', 'david']
your_user = input("Please type your name to see if you are blocked: ")

if your_user in banned_users:
    print("Do not go! Do not collect $200! ")
else:
    print("You are safe!")
```

Output:

```
Please type your name to see if you are blocked: jonathan
You are safe!

Please type your name to see if you are blocked: david
Do not go! Do not collect $200!
```

### 9. Checking Whether a Value is Not in a List

- You can use the keyword `not` check whether a value does not appear in a list.

```
banned_users = ['andrew', 'carolina', 'david']
your_user = input("Please type your name to see if you are blocked: ")

if your_user not in banned_users:
    print(f"{your_user.title()}, you are safe!")
else:
    print("Do not pass go! Do not collect $200!")
```

Output:

```
Please type your name to see if you are blocked: jonathan
Jonathan, you are safe!

Please type your name to see if you are blocked: andrew
Do not pass go! Do not collect $200!
```