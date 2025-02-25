#!/usr/bin/python3


"""
Module for defining and manipulating squares.

This module provides a Square class with methods to calculate area and perimeter.
"""

class Square:
    def __init__(self, side_length=0):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * 4
