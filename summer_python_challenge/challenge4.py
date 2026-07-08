num1 = input("Enter the first number.\n> ")
num2 = input("Enter the second number.\n> ")

if int(num1) > int(num2):
    print(f"{num1} is bigger than {num2}.")
elif int(num1) < int(num2):
    print(f"{num2} is bigger than {num1}.")
else:
    print(f"{num1} is the same as {num2}.")