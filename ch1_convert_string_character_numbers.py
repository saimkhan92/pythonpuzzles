# the program converts aaabbcccc into a3b2c4
a=input("input a string")

dict1={}
list1=[]

for i in a:
    if i in dict1.keys():
        temp=dict1[i]
        dict1[i]=temp+1
    else:
        dict1[i]=1

for i in sorted(dict1.keys()):
    list1.append(i)
    list1.append(str(dict1[i]))
print("".join(list1))
