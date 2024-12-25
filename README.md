
# Drawing the Indian National Flag using Python's Turtle Graphics

This Python project uses the `turtle` graphics library to draw a representation of the Indian national flag. The flag consists of three horizontal stripes of saffron, white, and green, along with a blue Ashoka Chakra at the center of the white stripe.

## Table of Contents

- Overview
- Requirements
- Code Explanation


## Overview

This script draws the Indian national flag using Python's `turtle` graphics module. It creates three colored rectangles representing the three stripes of the flag and an Ashoka Chakra with 24 spokes at the center of the white stripe.

## Requirements

- Python 3.x
- `turtle` module 

## Code Explanation

The script is structured as follows:

1. **`draw_rectangle(color)`**:
   - This function takes a color as an argument and draws a filled rectangle using the given color. It is used to create the three stripes of the flag.

2. **Turtle Setup**:
   - A turtle object `t` is created to draw the shapes.

3. **Drawing the Flag**:
   - The turtle moves to specific coordinates and draws the bottom green, middle white, and top saffron rectangles.

4. **Drawing the Ashoka Chakra**:
   - The script then draws the inner circle of the Ashoka Chakra, fills it with blue color, and draws 24 spokes from the center of the circle.
   - The outer circle of the Ashoka Chakra is drawn with a thicker pen size.

5. **Final Touches**:
   - The turtle is hidden after the drawing is completed, and `turtle.done()` is called to keep the window open.
