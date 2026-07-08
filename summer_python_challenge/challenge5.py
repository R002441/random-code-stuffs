num = input("Enter the number.\n> ")

if int(num) > 0:
    print(f"{num} is positive.")
elif int(num) < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")