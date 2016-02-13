# Python program to find the the mode of list

sequence=[1,1,1,1,1,1,2,4,5,6,7,2]
def arrayMode(sequence):
    dic={}
    count=0

    for i in range(0, len(sequence)):
        if sequence[i] in dic.keys():
            temp=dic[sequence[i]]
            temp=temp+1
            dic[sequence[i]]=temp
        else:
            dic[i]=1
            
    for k in dic.keys():
        temp=dic[k]
        break
    
    for k in dic.keys():
        if temp>dic[k]:
            break
        else:
            temp=dic[k]
            
    for k in dic.keys():
        if temp==dic[k]:
            print("The mode of the list is",end=" ")
            print(k)
            break


arrayMode(sequence)
