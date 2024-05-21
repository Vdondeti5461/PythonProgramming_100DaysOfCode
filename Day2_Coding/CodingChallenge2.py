height = input("Enter height:")
weight = input("Enter Weight:")

weight_as_int = int(weight)
height_as_float = float(height)

BMI = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(BMI)

print(bmi_as_int)

