#today we are going to code object orinented programming in python
class animal:
    def __init__(self,name,age):
      self.name = name
      self.age =age
    def bark(self):
      return f"{self.name} says woof!"
      x=53
      print(x)
my = animal("tom",52)
print(my.bark())
 

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!
#now we have finally achieved a way to code without being dependent on the system
