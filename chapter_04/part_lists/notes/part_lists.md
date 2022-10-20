## Working with Part of a List

1. Slicing a List:

- To make a slice, you specify the index of the first and last elements you want to work with. 

- As with the `range()` function, Python stops one item before the second index you specify.

- The following example involves a list of players on a team:

```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/part_lists$ python3 players.py
['charles', 'martina', 'michael']
```

NOTE: To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.

- You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:

```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_04/part_lists$ python3 players.py
['martina', 'michael', 'florence']
```

- If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:

```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```

Output:

```
['charles', 'martina', 'michael', 'florence']
```

2. Looping Through a Slice:

- You can use a slice in a `for` loop if you want to loop through a subset of the elements in a list. 

- In this example we loop through the first three players and print their names as part of a simple roster

```
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:\n")
for player in players[:3]:
    print(player.title())
```

Output:

```
Here are the first three players on my team:

Charles
Martina
Michael
```

3. Copying a List

- Often, you'll want to start with an existing list and make an entirely new list based on the first one. 

- To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).

- This example is in `foods.py`

```
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
```

Output:

```
My favorite foods are: 
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are: 
['pizza', 'falafel', 'carrot cake']
```

- Just to test that we actually have two separate lists, we can add a new food to each list

```
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
```

Output:

```
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'canoli']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
```