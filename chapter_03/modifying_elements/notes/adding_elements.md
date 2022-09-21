# Adding Elements to a List

### 1. You might want to add a new element to a list for many reasons.

- For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you've built. 

### 2. Appending Elements to the End of a List

- The simplest way to add a new element to a list is to *append* the item to the list. 

- When you append an item, the new element is added to the end of that list.

- This is how we can append `'ducati'` to the end of the list:

```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

### 3. The `append()` method makes it easy to build lists dynamically. 

- You can start with an empty list and then add items to the list using a series of `append()` calls. 

```
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki']
```

NOTE: Building lists this way is very common, because you often won't know the data your users want to store in a program until after the program is running. To put you users in control, start by defining an empty list that will hold the users' values.