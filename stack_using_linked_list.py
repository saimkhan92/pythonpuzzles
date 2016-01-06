class Node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n

class Stack(Node):
    def __init__(self):
        print("Stack object created")
        self.size=0
        self.root=None

    def push(self,d):
        node=Node()
        node.data=d
        node.next=self.root
        self.root=node
        self.size+=1
        
    def pop(self):
        if self.size==0:
            print("ERROR! ARRAY SIZE NULL")
            return False
        
        self.size=self.size-1
        temp=self.root
        self.root=temp.next
        return temp.data
        
    def display(self):
        if self.size==0:
            print("NO ELEMENTS TO DISPLAY")
        currentnode=self.root
        while currentnode:
            print(currentnode.data)
            currentnode=currentnode.next
            
if __name__=="__main__":
    
    
    obj1=Stack()
    obj1.push(2)
    obj1.push(4)
    obj1.push(6)
    obj1.push(8)
    obj1.push(10)
    obj1.push(10)
    obj1.push(14)
    obj1.display()
    
    obj1.pop()
    obj1.pop()
    print("\n")
    obj1.display()
    print("The size of stack is "+str(obj1.size))
    
    
    
    
    
        
        
