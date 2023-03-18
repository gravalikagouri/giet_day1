def func(n1, n2, n3, n4):
    print("num1=",n1,"num2=",n2,"num3=",n3,"num4=",n4)
func(12,21,211,221)
def func2(n1, n2, n3, n4):
    print("num1=",n1,"num2=",n2,"num3=",n3,"num4=",n4)
func2(n4=12,n2=21,n3=21,n1=12)
def func3(name,rollno,branch="cse",collegename="GIET"):
    print(name,rollno,branch,collegename)
func3("ravalika",12,"cse")
func3("nitish",21,"cse")
func3("nirav",121,"ece","gmr")
def func4(*var):#tuple
    for i in var:
        print(i,end=' ')
func4(12,122)
print()
func4(11,13,143,22)
print()
def add(*var):#tuple
    sum1=0
    for i in var:
        sum1=sum1+i
    print(sum1)
add(12,122)
print()
add(11,13,143,22)
print()
'''return sum1
print(add(10,20))'''
