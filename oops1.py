# initiate a class
class employee:
    # special method / magic method / dunder method - constructor
    def __init__(self):
        print(id(self))
        #print("started executing attribute / data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
       # print("attribute / data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")   


# creating an object /instance of the class
sam = employee()
print(id(sam))

#sam.travel("Kerala")
print(type(sam))