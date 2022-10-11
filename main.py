# 🚨 Entering height and weight👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#input type cheking👇
print(type(height))
print(type(weight))

# type conversion and bmi formula [bmi = weight / height**2]👇
bmi = int(weight) / float(height) ** 2

# bmi type cheking 👇
print(type(bmi))

# printing bmi result as interger
bmi_as_int = int(bmi)
print(bmi_as_int)







