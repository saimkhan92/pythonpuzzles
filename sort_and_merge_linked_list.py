# Join two sorted list list into a bigger linkedlist

class Node():
    def __init__(self,d=None,n=None):
        self.next=n
        self.data=d

class Linkedlist(Node):
    def __init__(self):
        self.root=None
        self.size=0
        
    def add(self,d):
             
        newnode=Node()
        newnode.data=d
        if self.size==0:
            self.root=newnode
        else:
            currentnode=self.root
            while currentnode.next:
                currentnode=currentnode.next
            currentnode.next=newnode
            newnode.next=None
        self.size+=1

        """
        # add node option2
        newnode=Node()
        newnode.next=self.root
        self.root=newnode
        newnode.data=d
        self.size+=1"""
            
    def display(self):
        currentnode=self.root
        while currentnode:
            print(currentnode.data,end="==>")
            currentnode=currentnode.next
        print("\n")        

if __name__=="__main__":
    obj1=Linkedlist()
    obj1.add(40)
    obj1.add(30)
    obj1.add(20)
    obj1.add(1)
    obj1.display()

    obj2=Linkedlist()
    obj2.add(55)
    obj2.add(25)
    obj2.add(23)
    obj2.add(21)
    obj2.add(0)
    obj2.display()

    def addsort(obj1,obj2):
        obj3=Linkedlist()
        current1=obj1.root
        current2=obj2.root
        size1=obj1.size
        size2=obj2.size

        while current1 and current2:
            if(int(current2.data)>int(current1.data)):
                obj3.add(current2.data)
                current2=current2.next
            else:
                obj3.add(current1.data)
                current1=current1.next

        while current1:
            obj3.add(current1.data)
            current1=current1.next

        while current2:                
            obj3.add(current2.data)
            current2=current2.next
        obj3.display()
    addsort(obj1,obj2)
            


            
                







    

    
