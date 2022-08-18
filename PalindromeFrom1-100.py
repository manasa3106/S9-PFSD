#palindrome
for i in range(1,100):
    temp=i
    r=0
    while i>0:
        dig=i%10
        r=r*10+dig
        i=i//10
    if(temp==r):
        print(temp)