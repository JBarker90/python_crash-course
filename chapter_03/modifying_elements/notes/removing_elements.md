# Removing Elements from a List

### 1. Often you'll want to remove an item or a set of items from a list. 

- For example, when a player shoots down an alien from the sky, you'll most likely want to remove it from the list of active aliens.

### 2. Removing an item using the `del` statement.

- If you know the position of the item you want to remove from a list, you can use the `del` statement.

```
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

del motorcyles[0]
print(motorcyles)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

- You can remove an item from any position in a list using the `del` statement if you know its index. 

- Here is how we can remove the second item, `'yamaha'`, in the list:

```
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

del motorcyles[1]
print(motorcyles)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']
```

### 3. Removing an item using the `pop()` method.

- Sometimes you'll want to use the value of an item after you remove it from a list. For example, you might want to get the *x* and *y*  position of an alien that was just shot down, so you can draw an explosion at that position. 

- The `pop()` method removes the last item in a list, but it lets you work with that item after removing it. 

- The term *pop* comes from thinking of a list as a stack of items and popping one item off the top of the stack. With that analogy, the top of the stack corresponds to the end of a list.

- Here is how we can pop a motorcyle from out list:

```
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

popped_motorcycle = motorcyles.pop()
print(motorcyles)
print(popped_motorcycle)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```

- How might this `pop()` method be useful? Imagine tha tthe motorcyles in the list are stored in chronological order according to when we owned them. 

- If this is the case, we can use the `pop()` method to print a statement about the last motorcyle we bought:

```
motorcyles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcyles.pop()
print(f"The last motorcyle I owned was a {last_owned.title()}")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
The last motorcyle I owned was a Suzuki
```

### 4. Popping items from any position in a list.

- You can use `pop()` to remove an item from any position in a list by including the index of the item you want to remove in parantheses. 

```
motorcyles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcyles.pop(0)
print(f"The last motorcyle I owned was a {first_owned.title()}")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
The last motorcyle I owned was a Honda
```

NOTE: If you’re unsure whether to use the del statement or the `pop()` method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the `del` statement; if you want to use an
item as you remove it, use the `pop()` method.

### 5. Removing an item by value.

- If you only know the value of the item you want to remove, you can use the `remove()` method. 

- For example, let's say we want to remove the value `'ducati'` from the list of motorcyles.

```
motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcyles)

motorcyles.remove('ducati')
print(motorcyles)
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```

- You can also use the `remove()` method to work with a value that's being removed from a list. 

- Here we can remove the value `'ducati'` and print a reason for removing it from the list:

```
motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcyles)

too_expensive = 'ducati'
motorcyles.remove(too_expensive)
print(motorcyles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_03/modifying_elements$ python3 motorcycles.py
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me.
```