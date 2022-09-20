# Using Individual Values from a List

### 1. You can use individual values from a list just as you would any other variable. 

- For example, you can use f-strings to create a message based on a value from a list.

- This will pull the first bicycle from the list and compose and message using the value.

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[-1].title()}."

print(message)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/intro_lists$ python3 bicycles.py
My first bicycle was a Specialized.
```