# Adding and Stripping Whitespace to Strings

### 1. Adding Whitespace to Strings with Tabs or Newlines

- In programming, `whitespace` refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols.
- You can use `whitespace` to organize your output for easier visibility

- To add a tab to your text, use the character combination `\t` as below:

```
>>> print("Python")
Python
>>> print("\tPython")
        Python
```

- To add a newline in a string, use the character combination `\n` as below:

```
>>> print("Languages:\nPython\nC\nJavascript")
Languages:
Python
C
Javascript
```

- You can also combine tabs and newlines in a single string. The string `"\n\t"` tells Python to move to a new line, and start the next line with a tab. 

```
>>> print("Languages:\n\tPython\n\tC\n\tJavascript")
Languages:
        Python
        C
        Javascript
```

### 2. Stripping Whitespace:

- Extra whitespace can be confusing in your programs. To programmers `'python'` and `'python '` look pretty much the same. But to a program, they are two different strings. 

- Python can look for extra whitespace on the right and left sides of a string. 

- To ensure that no whitespace exists at the right end of a string, us the `rstrip()` method

```
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>>
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '
```

NOTE: You can set the `favorite_language` variable as `'python '` and use `rstrip()` to remove the whitespace on the right side. However, it will only be removed temporarily. 

- To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:

```
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>>
>>> favorite_language
'python'
```

- You can also strip whitespace from the left side of a string using the `lstrip()` method, or from both sides at once using `strip()`

```
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'
```
