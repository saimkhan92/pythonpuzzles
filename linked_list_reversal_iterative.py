# Python linked list iterative reversal

class Node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n
        
class LinkedList(Node):
    def __init__(self):
        self.size=0
        self.root=None

    def addnode(self,d):            
        newnode=Node()
        newnode.data=d
        newnode.next=self.root
        self.root=newnode
        self.size=self.size+1
        
    def display(self):
        currentnode=self.root
        while currentnode:
            print(currentnode.data,end=" ==> ")
            currentnode=currentnode.next
        print("\n")

    def reverselist(self):
        currentnode=self.root
        prevnode=None
        currentnode=self.root
        nextnode=currentnode.next
        currentnode.next=prevnode


        while nextnode:            
            prevnode=currentnode
            currentnode=nextnode
            nextnode=currentnode.next
            currentnode.next=prevnode


        self.root=currentnode
        self.display()
        
        

if __name__=="__main__":

    obj1=LinkedList()
    obj1.addnode(10)
    obj1.addnode(20)
    obj1.addnode(30)
    obj1.addnode(60)
    obj1.addnode(40)
    obj1.addnode(5)
    obj1.display()
    print("\nreversing list\n")
    obj1.reverselist()

    





    
    
        
        
    
