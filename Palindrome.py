#palindrome
num=int(input("enter a number"))
temp=num
r=0
while(num>0):
    dig=num%10
    r=r*10+dig
    num=num//10
if(temp==r):
    print("the num is palindrome")
else:
    print("the num is not a palindrome")