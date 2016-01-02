import time
class Node:
    def __init__(self,d,n=None):
        self.next=n
        self.data=d
    def getnext(self):
        return self.next
    def getdata(self):
        return self.data
    def setnext(self,next1):
        self.next=next1
    def setdata(self,data1):
        self.data=data1
        
class LinkedList(Node):
    def __init__(self,root1=None):
        self.root=root1
        self.size=0
        
    def addnode(self,data1):
        node=Node(data1)
        node.setnext(self.root)
        self.root=node
        self.size+=1

    def displaylist(self):
        currentnode=self.root
        while currentnode:
            print(str(currentnode.getdata())+" --> ",end="")
            currentnode=currentnode.getnext()

    def reverse_iterative(self):
        current_node=self.root
        prev_node=None
        next_node=current_node.getnext()
        current_node.setnext(prev_node)
        while next_node:
            prev_node=current_node
            current_node=next_node
            next_node=next_node.getnext()
            current_node.setnext(prev_node)

        self.root=current_node
        
            
            
if __name__=="__main__":
    obj1=LinkedList()
    obj1.addnode(10)
    obj1.addnode(20)
    obj1.addnode(30)
    obj1.addnode(40)
    obj1.addnode(30)
    obj1.addnode(20)
    obj1.addnode(10)
    obj1.displaylist()


    print("\nreversing string\n")

    #obj1.reverse_iterative()

    #print("displaying reverse list")
    obj1.displaylist()

    def check_palindrom():
        obj2=obj1
        obj2.reverse_iterative()
      

        current_node1=obj1.root
        current_node2=obj2.root

        while current_node1:
            if current_node1.getdata()==current_node2.getdata():
                current_node1=current_node1.getnext()
                current_node2=current_node2.getnext()
            else:
                return False

        return True
        
        
        
        
        
    c=check_palindrom()        
    print(c)
    
    
        
        
        
    
        
