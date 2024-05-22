

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm ?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry , You have to grow taller before you can ride.")

# important things indentation and condition statement
#first if condition is true then check nested if else condition
#elif use for multiple conditions