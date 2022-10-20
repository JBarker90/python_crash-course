# A Simple Example of If Statement

### 1. The following short example shows how `if` tests let you respond to special situations correctly.

### 2. Imagine you have a list of cars and you want to print out the name of each car. However, the value 'bmw' should be printed in all uppercase.

- This code block loops through the list of cars in `cars.py` and then looks for 'bmw' to print uppercase

```
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

Output:

```
jonathan@dockerhost-01:~/python_crash-course/chapter_05/simple_if$ python3 cars.py
Audi
BMW
Subaru
Toyota
```