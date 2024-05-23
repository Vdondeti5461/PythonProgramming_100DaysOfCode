# leap year

year = int(input())

# checking the year is a leap year /not

if year % 4 == 0:
    if year % 100 == 0:
        if year % 100 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")

    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
