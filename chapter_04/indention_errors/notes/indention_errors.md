# Avoiding Indention Errors

### 1. As you begin to write code that relies on proper indention, you'll need to watch for a few common *indentation errors*.

### 2. Forgetting to Indent:

- Always indent the line after the `for` statement in a loop. If you forget, Python will remind you with a error.

```
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
print(magician)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/indention_errors$ python3 magicians_bad.py
  File "/home/jonathan/python_crash-course/chapter_04/indention_errors/magicians_bad.py", line 4
    print(magician)
    ^
IndentationError: expected an indented block after 'for' statement on line 3
```

### 3. Forgetting to Indent Additional Lines:

- Sometimes your loop will run without any errors but won't produce the expected result. This can happen when you're trying to do several tasks in a loop and you forget to indent some of its lines.

- For example, this is what happens when we forget to indent the second line in the loop that tells each magician we're looking forward to their next trick

```
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/indention_errors$ python3 magicians_bad.py
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

### 4. Indenting Unnecessarily:

- If you accidentally indent a line that doesn't need to be indented, Python informs you about the unexpected indent:

Example: In `hello_world.py`

```
message = "Hello Python World!"
    print(message)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/indention_errors$ python3 hello_world.py
  File "/home/jonathan/python_crash-course/chapter_04/indention_errors/hello_world.py", line 2
    print(message)
IndentationError: unexpected indent
```

### 5. Indenting Unnecessarily After the Loop:

- If you accidentally indent code that should run after a loop has finished, that code will be repeated once for each item in the list. 

- Sometimes this prompts Python to report an error, but often this will result in a logical error. 

```
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")
```

Output:

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show!
```

### 6. Forgetting the Colon:

- The colon at the end of a `for` statement tells Python to interpret the next line as the start of a loop.

- If you accidentally forget the colon, you'll get a syntax error because Python doesn't know what you're trying to do.

```
magicians = ['alice', 'david', 'carolina']

for magician in magicians
    print(magician)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/indention_errors$ python3 magicians_bad2.py
  File "/home/jonathan/python_crash-course/chapter_04/indention_errors/magicians_bad2.py", line 3
    for magician in magicians
                             ^
SyntaxError: expected ':'
```