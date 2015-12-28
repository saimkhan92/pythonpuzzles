string__m=input("please enter the master string")
string__s=input("please enter the slave string")
def is_substring(string_m,string_s):
    flag="not_check"
    dict={}
    list_test=[]
    string_m=list(string__m)
    string_s=list(string__s)
    print(string_m)
    print(string_s)

    first=string_s[0]
    last=string_s[len(string_s)-1]
    length_s=len(string_s)
    print("first element is "+first)
    print("last element is "+last)
    print("length of sub string is "+str(length_s))
    
    j=-1
    for i in string_m:
        j=j+1
        if i==first:
            list_test.append(j)
            
    print(list_test)
    
    for y in list_test:
        list_test1=[]
        print("\n")
        
        for i in range(y,y+length_s):
            try:
                print(string_m[i])
                list_test1.append(string_m[i])
            except IndexError:
                print("Index error. Hence not a substring.")
                return False
                
        if list_test1==string_s:
            print("MATCH! slave is a substring of master")
            return True
             
    return False    

a=is_substring(string__m,string__s)
print(a)
        
        
