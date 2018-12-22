
a=[]
for i in range (4):
    if(i==0):
        a[i]=int(input("enter"))
    else:
        c=int(input("enter"))
        while (i>0):
            if (c>a[i-1]):
                a[i]=a[i-1]
                a[i-1]=c
                i=i-1
print (a)                