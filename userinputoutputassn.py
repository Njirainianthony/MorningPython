#PROGRAM THAT RETURNS SMALLEST NUMBER AMONG 4 NUMBERS

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))
num4=int(input("Enter your fourth number: "))

if num1<num2 and num1<num3 and num1<num4:
    print(num1,"is the smallest number")
elif num2<num1 and num2<num3 and num2<num4:
    print(num2, "is the smallest number")
elif num3<num1 and num3<num2 and num3<num4:
    print(num3, "is the smallest number")
else:
    print(num4, "is the smallest number")


