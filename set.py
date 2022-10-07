# var = {"Geek", "hi", "football","SEM3","BYE"}
# print(var)







# set() methods is used to types conversion in Python.


# Python program to
# demonstrate sets
 
# Same as {"a", "b", "c"}
myset = set(("a", "b", "c"))
print(myset)
 
# Adding element to the set
myset.add("d")
print(myset)




















# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
""" normal_set = set(["a", "b","c"])

print("Normal Set")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set) """

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")
