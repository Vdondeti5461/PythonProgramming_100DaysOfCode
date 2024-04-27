# below len code  throw error because len function doesn't work with integers

# len(4532)


#
# num_char = len(input("what is your name?"))
# print("Your name has " +num_char + "characters")


# type casting converting one data type to another


num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

# print("Your name has {0}characters".format(new_num_char))

#type casting and conversion

a= float("2334")
print(a)
print(type(a))