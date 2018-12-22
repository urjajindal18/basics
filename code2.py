a=[]
n=int(input("Enter count "))
print("Enter list")
for i in range(n):
    if (i==0):
        a[i]=int(input("enter"))
    else :
        c=int(input("enter"))
        while(i>0):
            if(c<a[i-1]):
                a[i]=a[i-1]
                a[i-1]=c
print(a)            