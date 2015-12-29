m=int(input("enter the value of m "))
n=int(input("enter the value of n "))
dic={}


matrix=[[[] for i in range(n)] for i in range(m) ]

for i in range(int(m)):
    print("for row "+str(i))
    for j in range(int(n)):
        print("enter element "+str(j))
        user_input=int(input(""))
        matrix[i][j]=user_input
#print(matrix)

for i in range(int(m)):
    print("")
    for j in range(int(n)):
        print(matrix[i][j],end=" ")

for i in range(m):
    for j in range(n):
        if(matrix[i][j])==0:
            key=str(i)+"|||"+str(j)
            dic[key]=True

for i in dic.keys():
    x,y=i.split("|||")
    x=int(x)
    y=int(y)
    for i in range(m):
        matrix[i][x]=0
    for i in range(n):
        matrix[y][i]=0

print("\n The final matrix is \n")
for i in range(int(m)):
    print("")
    for j in range(int(n)):
        print(matrix[i][j],end=" ")

    

            


            

            
            
            
