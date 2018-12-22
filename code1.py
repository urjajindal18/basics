a=[]
count=int(input("Enter count"))
for i in range(count):
    print ("Enter element number ",i+1)
    c=int(input())
    a.append(c)
print("Original list given is ", a)
for i in range(count):
    a[i]=a[i]*a[i]
print ("Modified list is ",a)    
    

