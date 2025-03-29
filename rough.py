#lst = [1, 2, 3]
#my_str = "MLOPS playlist"
#my_int = 123

#print(type(my_str))

#lst.clear()
#my_str = my_str.capitalize()
#print(my_str)

from oops_proj import chatbook

user1 = chatbook()
print(user1.id)

# using static method from class rather then object
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)


# Getter and Setter
#print(user1.get_name())
#user1.set_name("Agent X")
#print(user1.get_name())

# function vs method below
#lst = [1, 2, 3]

#a1 = len(lst)
#print(a1)


