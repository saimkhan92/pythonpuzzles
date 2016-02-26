# check if a string a is a permutation of string b

a=input("enter first string")
b=input("enter second string")
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
