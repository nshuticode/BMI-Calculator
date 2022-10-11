# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#You will need to use "{:.2f}".format() in case you want two decimal places on your BMI number such as 24.22👇

bmi =round(weight/height**2)

if bmi < 18.5:
  # bmi_new_v = "{:.2f}".format(bmi)
  print(f"Your BMI is {bmi} , you are underweight.")
elif bmi < 25:
  # bmi_new_v = "{:.2f}".format(bmi)
  print(f"Your BMI is {bmi} , you have a normal weight.")
elif bmi < 30:
  # bmi_new_v = "{:.2f}".format(bmi)
  print(f"Your BMI is {bmi} , you are slightly overweight.")
elif bmi < 35:
  # bmi_new_v = "{:.2f}".format(bmi)
  print(f"Your BMI is {bmi} , you are obese.")
else:
  # bmi_new_v = "{:.2f}".format(bmi)
  print(f"Your BMI is {bmi} , you are clinically obese.")


