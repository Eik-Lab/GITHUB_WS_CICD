import math

def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError('Length and width must be positive numbers')
    return length * width

def circle_area(radius):
    if radius < 0:
        raise ValueError('Radius must be a positive number')
    return math.pi * radius**2

def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError('Base and height must be positive numbers')
    return 0.5 * base * height

def