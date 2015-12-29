
#check if slave is a rotation of master
string__m=input("please enter the master string")
string__s=input("please enter the slave string")

string_m1=list(string__m)
string_s1=list(string__s)
        
for i in range(len(string__m)):
    c=string_m1.pop()
    string_m1.insert(0,c)
    
    if string_m1==string_s1:
        print("MATCH!!")
        print("Slave is a rotation of master")
        raise SystemExit
print("Slave is not a rotation of master")

        
