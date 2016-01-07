class Node():
    def __init__(self,d=None,n=None):
        self.next=n
        self.data=d

class Stack():
    def __init__(self):
        self.size=0
        self.root=None
        self.max_size=5
        self.stack_no=0
        self.start_node=None
        
    def push(self,d):

        node=Node()
        if self.start_node==None:
            self.start_node=node
        node.data=d
        node.next=self.root
        self.root=node
        self.size+=1
        

    def pop(self):
        temp=self.root
        self.root=temp.next
        self.size-=1
        print(temp.data)
        if self.size==0:
            self.start_node=None
        return temp.data

    def display(self):
        currentnode=self.root
        while currentnode:
            print(currentnode.data)
            currentnode=currentnode.next
        print("\n")

    def delete_bottom(self):
        if self.size==0:
            print("EMPTY STACK NO BOTTOM")
        elif self.size==1:
            self.root=None
        else:    
            current_node=self.root
            while current_node:
                temp=current_node.next
                if temp==None:
                    return False
                if temp.next==None:
                    current_node.next=None
                print("test IN")
                current_node=current_node.next
                
        
        
if __name__=="__main__":

    # Plates are stacked in groups of max 5 plates, after 5 plates, a new group is initialized.
    # Pop() removes element from the previous group if the current stack is empty
    # max size set to 5 for testing purpose
    def plates():
        obj_list=[]
        obj_list.append(Stack())
        i=0
        while True:
            
            if obj_list[i].size<obj_list[i].max_size:
                x=input("select PUSH, POP or DISPLAY\n")
                if x=="PUSH":
                    y=input("enter number to push")
                    obj_list[i].push(y)
                elif x=="POP":
                    try:
                        obj_list[len(obj_list)-1].pop()
                        continue
                    except:
                        
                        if obj_list[len(obj_list)-1].size==0:
                            try:
                                obj_list[len(obj_list)-2].pop()
                            except:
                                print("ERROR!! NO ELEMENT FOUND")
                            
                elif x=="DISPLAY":
                    for j in obj_list:
                        j.display()

                elif x=="POP_NUM":
                    
                    p=int(input("\Enter the stack number from which you want to POP\n"))
                    stack_index=p-1                    
                    if stack_index==len(obj_list)-1:
                        obj_list[stack_index].pop()
                        
                    obj_list[stack_index].pop()
                    for q in range(stack_index,len(obj_list)-1):
                        
                        temp=obj_list[q+1].start_node
                        obj_list[q].push(temp.data)
                        obj_list[q+1].delete_bottom()
                        print("test out")
                
                elif x=="DONE":
                    break
                    
            else:
                obj_list.append(Stack())
                i=i+1
    plates()
            
            
        
        
        
        
