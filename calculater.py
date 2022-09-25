print("welcome to our calculater")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

a=  int(input("select number "))

if a==1:
    num1=int(input("enter your first number  "))
    num2=int(input("enter your second number  "))
    print(f"the addition of {num1}+{num2} is equal to {num1+num2}")

elif a==2:
    num1=int(input("enter your first number  "))
    num2=int(input("enter your second number  "))
    print(f"the subtraction of {num1}-{num2} is equal to {num1-num2}")
elif a==3:
    num1=int(input("enter your first number  "))
    num2=int(input("enter your second number  "))
    print(f"the multiplication of {num1}*{num2} is equal to {num1*num2}")
elif a==4:
    num1=int(input("enter your first number  "))
    num2=int(input("enter your second number  "))
    print(f"the division of {num1}/{num2} is equal to {num1/num2}")
else:
    print("  invalid syntax")
