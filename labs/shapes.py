"""Defines Shape and Rectangle classes"""

import math

class Shape():
  def __init__(self, num_sides, side_length):
    self.num_sides = num_sides
    self.side_length = side_length

  def calculate_area(self):
    n = self.num_sides
    l = self.side_length
    pi = 3.14
    return n * l * l / (4 * math.tan(pi/n))

class Rectangle(Shape):
  def __init__(self, height, width):
    super().__init__(4, height)
    self.height = height
    self.width = width

my_rectangle = Rectangle(3, 4)
print(my_rectangle.num_sides)
print(my_rectangle.calculate_area())
