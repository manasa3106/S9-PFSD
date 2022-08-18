#prime number
a=int(input("Enter a number"))
count=0
for i in range(1,a):
      num=a%i
      if num==0:
         count+=1
if count==1:
      print("prime number")
else:
    print("not a prime number")
