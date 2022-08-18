#swapnumbers
a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))     
print("before swap a and b are:",a,b)
a=a+b
b=a-b
a=a-b
print("after swap a and b are:",a,b)
