# bubble sort using while loop
list_a=[3,1,5,5,6,7,6,3,2,5,9,4,3]
print(list_a)
print("bubble sort begins")
listlen=len(list_a)

while True:
    j=0
    while j<listlen-1:
        if list_a[j]>list_a[j+1]:
            temp=list_a[j]
            list_a[j]=list_a[j+1]
            list_a[j+1]=temp
        j=j+1
        print(list_a)
    listlen=listlen-1
    print(listlen)
    if listlen==1:
        break

print("The sorted list is:",end=" ")
print(list_a)
