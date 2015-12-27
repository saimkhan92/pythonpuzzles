a=input("enter master string")
b=input("enter slave string")
dict={}
j=0

for i in a:
    dict[i]=True
for i in b:
    if i in dict.keys():
        if dict[i]==True:
            j=j+1
            dict[i]==False
if j==len(a):
    print("Slave is a permutation of the master")
else:
    print("not a permutation")
