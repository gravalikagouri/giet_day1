
n= int(input("enter the number:"))
if (n%3==0 and n%5==0):
    print("multiple of both 3 and 5")
elif(n%5==0):
    print("multiple of 5")
elif( n%3==0):
    print("multiple of both 3 ")
else:
    print("invalid")
    
