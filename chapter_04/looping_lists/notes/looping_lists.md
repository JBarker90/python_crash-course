## Looping Through an Entire List

1. When you want to do the same action with every item in a list, you can use Python's `for` loop.

- A `for` loop avoids both of these issues by letting Python manage these issues internally. 

- Let's use a `for` loop to print out each name in a list of magicians in our `magicians.py` file:

```
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04$ python3 magicians.py
alice
david
carolina
```

2. A Closer look at Looping:

- The concept of looping is important because it's one of the most common ways a computer automates repetitive tasks. 

- For example, in a simple loop like we used in `magicians.py`, Python initially reads the first line of the loop:

```
for magician in magicians:
```

- This line tells Python to retrieve the first value from the list magicians and associate it with the variable magician. 

- Then, python prints the current value of `magician`, which is `alice` and loops to do the same process with the next value.

```
print(magician)
```

3. Doing More Work Within a `for` Loop:

- Let's build on the previous example by printing a message to each magician, telling them that they performed a great trick:

```
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/looping_lists$ python3 magicians.py
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

- You can also write as many lines of code as you like in the `for` loop. Every indented line following the line `for magician in magicians` is considered *inside the loop*, and each indented line is executed once for each value in the list. 

- Let's add a second line to our message, telling each magician that we're looking forward to their next trick:

```
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/looping_lists$ python3 magicians.py
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

```

4. Doing Something After a `for` Loop:

- What happens once a `for` loop has finished executing? Usually, you'll want to summarize a block of output or move on to other work that your program must accomplish. 

- Any lines of code after the `for` loop that are not indented are executed once without repetition. 

```
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/looping_lists$ python3 magicians.py
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

NOTE: When you’re processing data using a for loop, you’ll find that this is a
good way to summarize an operation that was performed on an entire data
set. For example, you might use a for loop to initialize a game by running
through a list of characters and displaying each character on the screen.
You might then write some additional code after this loop that displays a
Play Now button after all the characters have been drawn to the screen.