# Using Variables in Strings

### 1. In some situations, you'll want to use a variable's value inside a string. 

- For example, you may want two variables to represent a first name and a last name respectively, and then want to combine those values to display someone's full name.

- Here we can create a new file called `full_name.py` to house the code

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

Output when run:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 full_name.py
ada lovelace
```

NOTE: To insert a variable’s value into a string, place the letter `f` immediately
before the opening quotation mark. Put braces around the name or names
of any variable you want to use inside the string. Python will replace each
variable with its value when the string is displayed.

- These strings are called `f-strings`. The `f` is for `format`, because Python
formats the string by replacing the name of any variable in braces with its
value.

### 2. You can do a lot with `f-strings`. For example, you can use `f-strings` to compose complete messages using the information associated with a variable:

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")
```

Output when run:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 full_name.py
Hello, Ada Lovelace!
```

### 3. You can also use `f-strings` to compose a message, and then assign the entire message to a variable.

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

message = f"Hello, {full_name.title()}!"
print(message)
```

NOTE: This code displays the message `Hello, Ada Lovelace!` as well, but by assisigning the `message` to a variable we make the final `print()` call much simpler. 

Output when run:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_02/strings$ python3 full_name_2.py
Hello, Ada Lovelace!
```
