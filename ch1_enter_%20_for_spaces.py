# program to replace space by %20
a=input("please enter a string")
list1=[]

for i in a:
    if i!=" ":
        list1.append(i)
    else:
        list1.append("%20")
print("".join(list1))
