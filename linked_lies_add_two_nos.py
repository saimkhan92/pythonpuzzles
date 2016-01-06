#some part of this is incomplete
class Node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n

class LinkedList(Node):
    def __init__(self,r=None):
        self.root=r
        self.size=0
        self.prevnode=None

    def addnode(self,d):
        node=Node()
        node.data=d
        node.next=self.root
        self.root=node
        self.size=self.size+1

    def addnode_forward(self,d):
        node=Node()
        node.data=d
        if not self.prevnode:
            self.prevnode=node
            self.root=node
        else:
            temp=self.prevnode
            temp.next=node
            self.prevnode=node
            
        
        self.size=self.size+1
        
        

    def displaylist(self):
        currentnode=self.root
        while currentnode:
            print(str(currentnode.data)+" --> ",end="")
            currentnode=currentnode.next



if __name__=="__main__":
    
    obj1=LinkedList()
    obj1.addnode_forward(6)
    obj1.addnode_forward(2)
    obj1.addnode_forward(9)
    obj1.addnode_forward(1)

    obj1.displaylist()
    print("\nsize of the list: "+str(obj1.size))

    obj2=LinkedList()
    obj2.addnode_forward(6)
    obj2.addnode_forward(9)


    if abs(obj1.size-obj2.size)>0:
        temp1=abs(obj1.size-obj2.size)
        #print("absolute value "+str(temp1))
        obj3=LinkedList()
        
        if obj1.size>obj2.size:
            for i in range(obj1.size-obj2.size):
                obj3.addnode_forward(0)
            currentnode=obj2.root

            while currentnode:
                obj3.addnode_forward(currentnode.data)
                currentnode=currentnode.next
                
        

    obj3.displaylist()
    print("\nsize of the list: "+str(obj2.size))

    def add(obj1,obj2):
        current1=obj1.root
        current2=obj3.root
        obj4=LinkedList()
        z1prev=0
        z2prev=0
        while current1:
            z=int(current1.data)+int(current2.data)
            print(z)
            z1=int(z/10)
            z2=int(z%10)
            obj4.addnode_forward(z2+z1prev)
            z1prev=z1
            z2prev=z2
            print(z1)
            print(z2)
            
            current1=current1.next
            current2=current2.next
        #print(z)
        if z1>0:
            obj4.addnode_forward(z1)
            
        obj4.displaylist()


    add(obj1,obj2)
    
    










        

    
    
