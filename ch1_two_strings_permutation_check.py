a=input("enter master string")
b=input("enter slave string")
dict={}
list1=[0]*256

for i in a:
    list1[ord(i)]=list1[ord(i)]+1

for i in b:
    if list1[ord(i)]==0:
        print("Not a permutation")
        raise SystemExit
    if list1[ord(i)]>0:
        list1[ord(i)]=list1[ord(i)]-1

for i in list1:
    if i==0:
        j=True
    else:
        print("not permutation")
        raise SystemExit
print("It is a valid permutation")
