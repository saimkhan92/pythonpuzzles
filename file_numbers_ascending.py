# print all numbers of a wikipedia page in ascending order in a new output file
# using inbuilt sort function not allowed

import os
import re

print(os.getcwd())

with open("wikipedia india.txt") as fh:
    text=fh.read()
    re_list=re.findall("[0-9]+",text)
    #print(re_list)
re_list=[float(i) for i in re_list]

for i in range(len(re_list)):
    for j in range(len(re_list)):
        if re_list[i]<re_list[j]:
            temp=re_list[j]
            re_list[j]=re_list[i]
            re_list[i]=temp
            
for i in re_list:
    print(i)


        
        
    
