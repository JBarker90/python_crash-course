# Accessing Elements in a List

### 1. Lists are ordered collections, so you can access any element in a list by telling Python the position, or *index* of the item desired. 

### 2. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets. 

- For example, let's pull out the first bicycle in the list bicycles:

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/intro_lists$ python3 bicycles.py
trek
```

### 3. You can also use the string methods from Chapter 2 on any element in this list. 

- For example, you can format the element `'trek'` more neatly by using the `title()` method:

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/intro_lists$ python3 bicycles.py
Trek
```