l=[18,20,8,16,4,10,12,3]
a=max(l)
c=0
if a%2==0:
    a=a/2
    c+=1
else:
    a=a-1
    c+=1
print(c)