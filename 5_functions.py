#functions
def func1():
    print("functions")
func1()
def func2(num1,num2):
    print("num1 =" ,num1,"num2 =", num2)
func2(21,12)
def func3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",func3(21,12))
def func4(num1,num2):
    num3=num1+num2
    return num3
print("value returned",func4(21,12.21))
def func5(num1,num2):
    num3=float(num1)+num2
    return num3
print("value returned",func5('21',12.21))
def func6(num1,num2):
    num3=num1+str(num2)
    return num3
print("value returned",func6("ravalika ",12.21))
