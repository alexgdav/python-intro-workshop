"""Defines a CoffeeCup Class"""

class CoffeeCup():
  def __init__(self, capacity, amount = 0):
    self.capacity = capacity
    self.amount = amount

  def fill(self):
    self.amount = self.capacity

  def empty(self):
    self.amount = 0

  def drink(self, param):
    if self.amount == 0:
      print ("The cup is empty")
    elif self.amount < param:
      print ("There's not enough coffee")
    else:
      self.amount -= param

cup = CoffeeCup(5)
cup.fill()
print(cup.amount)
cup.drink(4)
print(cup.amount)
cup.drink(5)
print(cup.amount)
