list1=[18,20,8,16,4,10,12,3]
va=list1.sort()
num=list1[-2]
count=0
while num!=0:
    if(num%2==0):
        num=num//2
        count+=1
    elif(num%2!=0):
         num=num-1
         count+=1
print(count)
            
            