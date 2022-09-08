# Running Hello World Program

### 1. This will be a simple `print` statement. Create a file called `hello_world.py` and add the following

```
print("Hello Python world!")
```

### 2. In VS Code you can run it using the run button. However, from the terminal you can run the program using the `python3` command

```
jonathan@dockerhost-01:~/python_crash-course/chapter_01$ python3 hello_world.py
Hello Python world!
```

### 3. If there is a syntax error, Python will tell you. I created a test file with extra character to break python called `hello_world-bad.py`

```
jonathan@dockerhost-01:~/python_crash-course/chapter_01$ python3 hello_world-bad.py
  File "/home/jonathan/python_crash-course/chapter_01/hello_world-bad.py", line 1
    print("This is to test bad code."{)
                                      ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
```
