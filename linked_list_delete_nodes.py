# Linked delete node program

import time
class Node():
    def __init__(self, d, n):
        self.next_node=n
        self.data=d
    def getnext(self):
        return self.next_node
        
    def setnext(self,nxt):
        self.next_node=nxt

    def setdata(self,data1):
        self.data=data1

    def getdata(self):
        return self.data

class LinkedList(Node):
    def __init__(self,root1=None):
        self.root=root1
        self.size=0
    def getsize(self):
        return self.size

    def find(self, data1):
        currentnode=self.root
        while currentnode:
            if currentnode.getdata()==data1:
                return data1
            else:
                currentnode=currentnode.getnext()
        return False
            
    def addnode(self,data1):
        newnode= Node(data1,self.root)
        self.root=newnode
        self.size+=1
        
    def deletenode(self,data1):
        currentnode=self.root
        previousnode=None
        while currentnode:
            if currentnode.getdata()==data1:
                if previousnode:
                    previousnode.setnext(currentnode.getnext())
                else:
                    self.root=currentnode.getnext()
                self.size-=1
                return True
            else:
                previousnode=currentnode
                currentnode=currentnode.getnext()
        return False

    def display_list(self):
        currentnode=self.root
        while currentnode:
            print(currentnode.getdata())
            currentnode=currentnode.getnext()
            
    def display_from(self,k):
        n=0
        currentnode=self.root
        while currentnode:
            n=n+1
            if n>=k: 
                print(currentnode.getdata())
            currentnode=currentnode.getnext()
        
 

                        
    
if __name__=="__main__":

    

    obj=LinkedList()
    d=obj.getsize()
    print("SIZE OF THE LIST IS {}\n".format(d))
    print("Adding nodes to linked list")
    obj.addnode(20)
    obj.addnode(30)
    obj.addnode(10)
    obj.addnode(20)
    obj.addnode(10)
    obj.addnode(10)
    obj.addnode(20)
    obj.addnode(50)

    print("the list nodes are: \n")
    obj.display_from(3)
    
        

    
        
        
