class Item:
  
  all = [] # object attributes
  def __init__(self, name, price, quantity):
    # run validation to the received arguments
    assert price >= 1, f"Price {price} should not be less than 1"
    assert quantity >= 1, f"Quantity {quantity} should not be less than 1"
    
    # assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity
    
    Item.all.append(self)
    
  def result(self):
    print(f"Hello mr.{self.name}, welcome to the BruhLars")
  
  # class method - a function that belong to the object or class
  def __repr__(self):
    return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
  

item1 = Item("Jeremy", 200, 3)
item2 = Item("Bem", 400, 2)
item3 = Item("Jem", 150, 5)
item4 = Item("Cherry Mae", 1000, 2)
item1.result()
for instance in Item.all:
  print(instance.name)