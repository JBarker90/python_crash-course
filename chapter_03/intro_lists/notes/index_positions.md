## Index Positions Start at 0, Not 1

1. Python considers the first item in a list to be at position 0, not position 1. This is true of most programming languages. 

2. The second item in a list has an index of 1. Using this system, you can get any element you want from a list by subtracting one from its position in the list. 

- The following asks for the bicycles at index 1 and index 3:

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/intro_lists$ python3 bicycles.py
cannondale
specialized
```

3. Python has a special syntax for accessing the last element in a list. 

- By specifying the item at index -1, Python always returns the last item in the list:

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/intro_lists$ python3 bicycles.py
specialized
```

NOTE: The index -2 returns the second item from the end, the index -3 returns the third item from the end, and so forth.