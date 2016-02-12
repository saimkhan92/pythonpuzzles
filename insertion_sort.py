# python implementation of insertion sort

l=[2,4,1,3,6,8,7]

for i in range(0,len(l)-1):
    while i>=0:
        if l[i]>l[i+1]:
            temp=l[i+1]
            l[i+1]=l[i]
            l[i]=temp

            print(l)
        else:
            break
        i=i-1

print(l)
