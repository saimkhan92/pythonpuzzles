#implementation of a linked list

class Node():
    def __init__(self, d, n=None,p=None):
        self.next_node=n
        self.prev_node=p
        self.data=d
    def getnext(self):
        return self.next_node
        
    def setnext(self,nxt):
        self.next_node=nxt


    def getprev(self):
        return self.prev_node
        
    def setprev(self,prev1):
        self.prev_node=prev1


    
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
        if self.root:
            self.root.setprev(newnode)
        self.root=newnode
        self.size+=1
        
    def deletenode(self,data1):
        currentnode=self.root
        while currentnode:
            if currentnode.getdata()==data1:
                next=currentnode.getnext()
                prev=currentnode.getprev()

                if next:
                    next.setprev(prev)
                if prev:
                    prev.setnext(next)
                else:
                    self.root=currentnode.getnext()
                    
                self.size-=1
                return True
            else:
                currentnode=currentnode.getnext()
        return False
                
    
if __name__=="__main__":
    obj=LinkedList()
    d=obj.getsize()
    print("SIZE OF THE LIST IS {}".format(d))
    obj.addnode(10)
    obj.addnode(330)
    obj.addnode(12)
    obj.addnode(104)
    obj.addnode(1022)
    obj.addnode(101)
    a=obj.find(101)
    d=obj.getsize()
    print("SIZE OF THE LIST IS {}".format(d))
    
    print("FIND 101 RESULT: {}".format(a))
    b=obj.find(111111111)
    print("FIND 11111111 RESULT: {}".format(b))
    
    c=obj.deletenode(330)
    if c:
        print("{} node deleted".format(330))
        
    n=obj.find(330)
    print("FIND 330 RESULT: {}".format(n))
    
    d=obj.getsize()
    print("SIZE OF THE LIST IS {}".format(d))



    
        

    
        
        
