# Program will make a user input the matrix. The program will then put zero in the row and column whereever a zero is encountered in the matrix

"""
#Method to declare matrix using list comprehension

from random import randint
rows=int(input("Please enter the number of rows in the matrix"))
columns=int(input("Please enter the number of columns in the matrix"))
matrix=[[[randint(0,4)] for i in range(columns)] for j in range(rows)]
print("The following matrix has been generated")
for i in matrix:
    print(i)   
"""

matrix=[[1,2,3,4],[2,8,0,5],[33,1,5,6],[1,0,4,3],[2,5,1,4]]
rows=len(matrix)
columns=len(matrix[0])
visited={}
#for i in matrix:
#    print(i)
#print("\n")

for i in range(rows):                           # mark the matrix nodes not visited to "no"
    for j in range(columns):
        visited[(i,j)]="no"

for i in range(rows):
    for j in range(columns):
        if visited[(i,j)]=="no":
            if matrix[i][j]==0:                 # if zero is encountered
                for x in range(rows):
                    matrix[x][j]=0
                    visited[(x,j)]="yes"        # if visited, mark the node to "yes"
                for y in range(columns):
                    matrix[i][y]=0
                    visited[(i,y)]="yes"   
            else:
                visited[(i,j)]="yes"
        else:
            continue 

print("The final matrix is")
for i in matrix:
    print(i)

    
