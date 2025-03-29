# Single or Basic Inhetetence

# Base class
#class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived Class
#class Child(Parent):
#    def play(self):
#        print(f"{self.name} is playing.")

# Create an instance of child
#child = Child("Alice")
#child.greet()   # Output : Hello, my name is Alice.
#child.play()     # Output : Alice is playing.


# Multilevel Inheretence

# Base Class
#class Grandparent:
#    def __init__(self, name):
#        self.name = name

#    def tell_story(self):
#        print(f"{self.name} tells a story.")

# Intermediate class
#class Parent(Grandparent):
#    def work(self):
#        print(f"{self.name} is working.")

# Derived class
#class Child(Parent):
#    def play(self):
#        print(f"{self.name} is playing. ")

# Create ann instance of child
#child = Child("Charlie")
#child.tell_story()   # Output : Charlie tells a story
#child.work()         # Output : Charlie is working
#child.play()         # Output : Charlie is playing




# Hiererchical Inheretence

# Base class
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived class 1
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Derived class 2
class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying.")

# create instances of Child 1 and Child 2
child1 = Child1("Dave")
child2 = Child2("Eve")

child1.greet()      # Output : Hello, my name is Dave.
child1.play()       # Output : Dave is playing.

child2.greet()      # Output : Hello, my name is Eve.
child2.play()       # Output : Eve is studying.