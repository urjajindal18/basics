a=[]
count=int(input("Enter count"))
for i in range(count):
    print ("Enter element number ",i+1)
    c=int(input())
    a.append(c)
print (a)
for i in range(count):
     while(i < count-1):
         if(a[i]<a[i+1]):
             d=a[i+1]
             a[i+1]=a[i]
             a[i]=d
             i=i+1
             
        
