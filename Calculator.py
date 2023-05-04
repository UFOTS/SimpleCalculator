para = """Hello!!! 
This is a simple calculator"""

print(para)

print("You can use this calculator to add,subtract,multiply,divide,find power,remainder!!!")

def add():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(num1,"+",num2,"=",num1+num2)

def sub():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(num1,"-",num2,"=",num1-num2)

def mul():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(num1,"x",num2,"=",num1*num2)

def div():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(num1,"/",num2,"=",num1/num2)

def pow():
    num1 = int(input("Enter the number : "))
    num2 = int(input("Enter the power : "))
    print(num1,"^",num2,"=",num1**num2)

def rem():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(num1,"%",num2,"=",num1%num2)

ts = input("What kind of operation you want ? ")

if "add" in ts:
    add()
elif "sub" in ts:
    sub()
elif "mul" in ts:
    mul()
elif "div" in ts:
    div()
elif "pow" in ts:
    pow()
elif "rem" in ts:
    rem()
else:
    print("Type correctly")

print("Thank You !!! This Is Made By T.Sujeeth")