#primenumbers between 1 to 100
for a in range(2,100):
    count=0
    for i in range(1,a):
        num=a%i
        if num==0:
            count+=1
    if count==1:
        print(a)