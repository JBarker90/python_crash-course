# Strings

### 1. A `string` is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this:

```
"This is a string."
'This is also a string.'
```

- This gives you flexibillity to use quotes and apostrophes within your strings:

```
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

### 2. Changing Case in a String with Methods

- One of the simplest tasks you can do with strings is change the case fo the words in a string. 
- Here we can create a new file called `name.py` and add the following:

```
name = "ada lovelace"
print(name.title())
```

NOTE: When you run this the `name.title()` method will capitalize the letters in the name

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 name.py
Ada Lovelace
```

- In this example, the variable `name` refers to the lowercase string `"ada lovelace"`. The method `title()` appears after the variable in the `print()` call. 

- A `method` is an action that Python can perform on a piece of data. The dot (.) after `name` in `name.title()` tells Python to make the `title()` method act on the variable `name`.

- Several other useful methods are available for dealing with case as well. You can change a string to all uppercase or all lower case letter like this:

```
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

Output when run:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 name_2.py 
ADA LOVELACE
ada lovelace
```