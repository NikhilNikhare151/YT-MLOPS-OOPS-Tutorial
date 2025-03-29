# simple inheretence
# Base class
#class Animal:
 #   def __init__(self, name):
 #       self.name = name

 #   def speak(self):
 #       print(f"{self.name} makes a sound.")

    
# Derived class
#class Dog(Animal):
 #   def __init__(self):
 #       self.behavoir = "Friendly"

  #  def speak(self):
 #       print(f"Buddy barks. He is very {self.behavoir}")

# create an instance of animal
#animal = Animal("Generic Animal")
#animal.speak()  # Output : Generic Animal makes a sound

# create an instance of dog
#dog = Dog()
#dog.speak()   # Output : Buddy barks


# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.namd} makes a sound")

# Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()   # call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# Create an instance of Dog
dog = Dog("Golden Retriver")
dog.speak()
# Output : 
# Buddy makes a sound
# Buddy barks. It is a Golden Retriver