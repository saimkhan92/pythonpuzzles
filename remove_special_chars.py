# program to read from a file, remove all numbers and special characters, make a new modified result file
# place file in the same directory as the python program

import re
import os

print(os.getcwd())

fh=open("census.txt","r")
file_text=fh.read()
#file_list=file_text.split()

#print(file_list)
alphabets=re.findall(r"[A-Z,a-z]+",file_text)
print(alphabets)
fh1=open("census_new.txt","a")

for i in alphabets:
    fh1.write(i)
    fh1.write(" ")
    
fh1.close()
fh.close()


