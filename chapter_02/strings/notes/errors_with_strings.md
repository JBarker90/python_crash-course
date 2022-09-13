## Avoiding Syntax Errors with Strings

1. A *syntax error* occurs when Python doesn't recognize a section of your program as valid Python code.

- For example, if you use an apostrophe within single quotes, you'll produce an error.

2. Here's how to use single and double quotes correctly. Save this program as `apostrophe.py` and then run it:

```
message = "One of Python's strengths is its diverse community."
print(message)
```

Run output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 apostrophe.py
One of Python's strengths is its diverse community.
```

3. However, if you use single quotes, Python can't identify it and it will break with a syntax error:

```
message = 'One of Python's strengths is its diverse community.'
print(message)
```

Run output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 apostrophe_error.py
  File "/home/jonathan/python_crash-course/chapter_02/strings/apostrophe_error.py", line 1
    message = 'One of Python's strengths is its diverse community.'
                                                                  ^
SyntaxError: unterminated string literal (detected at line 1)
```
