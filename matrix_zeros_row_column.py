# Program will make a user input the matrix. The program will then put zero in the row and column whereever a zero is encountered in the matrix




rows=input("Please enter the number of rows in the matrix")
columns=input("Please enter the number of columns in the matrix")
matrix=[[[None] for column in columns] for row in rows]
print(matrix)
