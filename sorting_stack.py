# Sort a stack in ascending order using max one more stack

def display(stack_t):
    print("\n")
    for i in reversed(range(0,len(stack_t))):
        print(stack_t[i])

def peek(stack_t):
    return stack_t[len(stack_t)-1]

    
stack1=[4,2,3,4,66,767,33,1,76]
stack2=[]

display(stack1)

while len(stack1)!=0:
    temp=stack1.pop()
    if len(stack2)==0:
        stack2.append(temp)
        
    else:
        while stack2:
            if temp<peek(stack2):
                stack1.append(stack2.pop())
                
            else:
                break
        stack2.append(temp)
        
display(stack2)    
