#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(10)
print("{} - {} => {} / {}".format(
    my_rectangle.width,
    my_rectangle.height,
    my_rectangle.area(),
    my_rectangle.perimeter()))
