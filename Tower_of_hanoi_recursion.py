# Tower of hanoi problem solution

def tower_of_hanoi(n,source,buffer,destination):
    if n>0:
        tower_of_hanoi(n-1,source,destination,buffer)
        if source:
            temp=source.pop()
            destination.append(temp)
        tower_of_hanoi(n-1,buffer,source,destination)


source=[5,4,3,2,1]
buffer=[]
target=[]

tower_of_hanoi(len(source),source,buffer,target)
print(source)
print(buffer)
print(target)
