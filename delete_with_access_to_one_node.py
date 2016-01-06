class Node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n
        

class LinkedList(Node):
    def __init__(self):
        self.root=None
        self.size=0
        self.last=None
        
    def addnode(self,d):
        node=Node()
        if not self.last:
            self.last=node
        
        node.data=d
        node.next=self.root
        self.root=node
        

    def displaylist(self):
        currentnode=self.root
        while currentnode:
            print(str(currentnode.data)+" --> ",end="")
            currentnode=currentnode.next
        print("\n")

        
if __name__=="__main__":
    obj1=LinkedList()
    obj1.addnode(1)
    obj1.addnode(21)
    obj1.addnode(32)
    obj1.addnode(443)
    obj1.addnode(22)
    obj1.addnode(26)
    obj1.addnode(10)
    obj1.addnode(10)
    obj1.addnode(446)
    obj1.addnode(23)
    obj1.addnode(26)
    obj1.addnode(17)
    obj1.addnode(61)

    obj1.displaylist()

    k=26
   
    obj_equal=LinkedList()
    obj_less=LinkedList()
    obj_greater=LinkedList()
    currentnode=obj1.root

    while currentnode:
        if currentnode.data==k:
            obj_equal.addnode(currentnode.data)
        elif currentnode.data>k:
            obj_greater.addnode(currentnode.data)
        elif currentnode.data<k:
            obj_less.addnode(currentnode.data)
        currentnode=currentnode.next

    #obj_less.displaylist()
    #obj_equal.displaylist()
    #obj_greater.displaylist()

    last_less=obj_less.last
    last_equal=obj_equal.last
    last_greater=obj_greater.last
    
    last_less.next=obj_equal.root
    last_equal.next=obj_greater.root
    obj_less.displaylist()

    print("\n##########PRE DELETION##########\n")



    ###############################THIS PROGRAM STARTS HERE##############################################
    # GIVEN ACCESS TO A NODE (last_less) HOW WOULD YOU DELETE THAT NODE

    print("item to be deleted")
    print(last_less.data)
    next_addr=last_less.next
    next_data=next_addr.data
    last_less.data=next_data
    last_less.next=next_addr.next
    
    print("\n##########POST DELETION##########\n")
    obj_less.displaylist()
    
        
                
        





        
