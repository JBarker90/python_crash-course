# Modifying Elements in a List

### 1. Changing, Adding, and Removing Elements:

- Most lists you create will be dynamic, menaing you'll build a list and then add and remove elements from it as your program runs its course. 

- For example, you might create a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. 

### 2. The syntax for modifying an element is similiar to the syntax for accessing an element in a list.

- To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

- For example, if we have a list of motorcycles and the first value is `'honda'` then we can change the value like this:

```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

NOTE: The code in the original list defines `'honda'` as the first element. The code in the second changes the value of the first item to `'ducati'`. 