#BMI calculator

height = input("Enter height:")
weight = input("Enter Weight:")

weight_as_int = int(weight)
height_as_float = float(height)

BMI = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(BMI)

if bmi_as_int <18.5:
    print(f"Your BMI is {bmi_as_int} , you are underweight.")
elif bmi_as_int <25:
    print(f"Your BMI is {bmi_as_int} , you are normal weight.")
elif bmi_as_int < 30:
    print(f"Your BMI is {bmi_as_int} , you are slightly overweight.")
else:
    print(f"Your BMI is {bmi_as_int} , you are obese.")

