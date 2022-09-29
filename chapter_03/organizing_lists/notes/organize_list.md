# Organizing a List

### 1. Sorting a List Permanently with the `sort()` Method

- Python's `sort()` method makes it relatively easy to sort a list. 

- Imagine we have a list of cars and want to change the order of the list to store them alphabetically. 

- To keep it simple, let's assume that all the values in the list are lowercase in our `cars.py` file:

```
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
['audi', 'bmw', 'subaru', 'toyota']
```

- You can also sort this list in reverse alphabetical order by passing the argument `reverse=True` to the `sort()` method.

```
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
['toyota', 'subaru', 'bmw', 'audi']
```

NOTE: Here is a proof of concept that the `sort()` function is permanent

```
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sort function:")
cars.sort()
print(cars)

print("\nHere is the original list again:")
print(cars)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sort function:
['audi', 'bmw', 'subaru', 'toyota']

Here is the original list again:
['audi', 'bmw', 'subaru', 'toyota']
```


### 2. Sorting a List Temporarily with the `sorted()` Function

- To maintain the original order of a list but present it in a sorted order, you can use the `sorted()` function. 

- The `sorted()` function lets you display your list in a particular order but doesn't affect the actual order of the list.

```
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
```

### 3. Printing a List in Reverse Order

- To reverse the original order of a list, you can use the `reverse()` method. 

- The `reverse()` doesn't sort backward alphabetically; it simply reverses the order of the list.

```
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("This is the original list:")
print(cars)

cars.reverse()

print("\nThis is the list in reverse:")
print(cars)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
This is the original list:
['bmw', 'audi', 'toyota', 'subaru']

This is the list in reverse:
['subaru', 'toyota', 'audi', 'bmw']
```

NOTE: The `reverse()` method changes the order of a list permanently, but you can revert to the original order anytime by applying `reverse()` to the same list a second time. 

### 4. Finding the Length of a List:

- You can quickly find the length of a list by using the `len()` function. 

- The list in this example has four items, so its length is 4:

```
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("The number of items in this list is: ", len(cars))
```

- You can also use this alternative syntax in a print statement. You just need to surround the `len()` function with a `,` comma.

```
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("There are ", len(cars),"items in this list.")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
The number of items in this list is:  4

jonathan@dockerhost-01:~/python_crash-course/chapter_03/organizing_lists$ python3 cars.py
There are  4 items in this list.
```

NOTE: You'll find `len()` useful when you need to identify the number of aliens that still need to be shot down in a game, determine the amount of data you have to manage in a visualization, or figure out the number of registered users on a websitem among other tasks.
