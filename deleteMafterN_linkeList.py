# delete n nodes after m nodes of a lined list

class node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n

class LinkedList():
    def __init__(self, r=None):
        self.size=0
        self.root=r

    def add(self,data):
        newnode= node(data)
        newnode.next=self.root
        self.root=newnode

    def display(self):
        currentnode=self.root
        while currentnode:
            print(str(currentnode.data)+" ==> ",end="")
            currentnode=currentnode.next

    def delete__n_after_m(self,n,m):
        currentnode=self.root
        c=1
        d=0
        while currentnode:
            c=c+1
            currentnode=currentnode.next
            if c==m:
                for i in range(n):
                   temp=currentnode.next
                   currentnode.next=temp.next
                print(" \n Deletions Completed")
                return True
               


obj=LinkedList()
obj.add(1)
obj.add(5)
obj.add(3)
obj.add(11)
obj.add(32)
obj.add(16)
obj.add(21)
obj.add(23)
obj.add(663)
obj.add(23)
obj.add(48)
obj.add(28)
obj.add(23)
obj.add(42)
obj.add(55)


obj.display()
            
obj.delete__n_after_m(3,5)
obj.display()
