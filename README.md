# Python Cheat Sheet

## Variables
```python
# Variables + Data Types
x = 10      # Integer
y = 3.14    # Float
name = "Alice"  # String
is_active = True  # Boolean
```

## Lists
```python
# Lists
my_list = [1, 2, 3, 4]
my_list.append(5)  # Add element
my_list.remove(3)  # Remove element
len(my_list) # Returns the size of the list (you'll need to store it in a variable)
```

## Control Flow
```python
# If-Else
x = 10
if x > 5:
    print("Greater than 5")
elif x == 5:
    print("Equal to 5")
else:
    print("Less than 5")

# Loops
for i in range(5):  # 0 to 4
    print(i)

while x > 0:
    print(x)
    x -= 1
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Modules & Imports
```python
import math
print(math.sqrt(16))

from datetime import datetime
print(datetime.now())
```

# Turtle Basics

## Introduction
`turtle` is a built-in Python module used for creating simple graphics. It provides an easy way to draw shapes, patterns, and animations.

## Getting Started
```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set speed (1-10, 0 for instant)
t.speed(3)

# Move the turtle forward
t.forward(100) # Number inside represents how many pixels

# Turn the turtle
t.left(90) # Number is how many degrees
t.forward(100)

# Close the window on click
turtle.done()
```

## Drawing Shapes
```python
# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Draw a circle
t.circle(50)

# Complete drawing
turtle.done()
```

## Changing Appearance
```python
# Change outline color
t.pencolor("blue")

# Change fill color
t.fillcolor("red")
t.begin_fill()
# <--- Put code for anything you want filled --->
t.end_fill()

# Change pen size
t.pensize(5)

# Hide turtle
t.hideturtle()
```

## Move without drawing
```python
# Raise pen up
t.penup()

# Raise pen down
t.pendown()

# Goes to that (x, y) coordinates
t.goto(-50, 50)
```



