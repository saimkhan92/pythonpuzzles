# Stack push pop and minimum element return

class Node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n

class Stack(Node):
    def __init__(self):
        self.size=0
        self.top=None
        self.min=None
        self.min_dict={}
        
    def push(self, d):
        node=Node()
        node.data=d
        node.next=self.top
        self.top=node
        self.size+=1
        if self.min==None:
            self.min=d
        if d<self.min:    
            self.min=d
        self.min_dict[self.size]=self.min
        

    def pop(self):
        temp=self.top
        self.root=temp.next
        self.size-=1
        return temp.data

    def display(self):
        current_node=self.top
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        print("\n")
    def get_min(self):
        print("Minimum element is : "+str(self.min_dict[self.size]))

if __name__=="__main__":
    obj1=Stack()
    obj1.push(17)
    obj1.push(20)
    obj1.push(30)
    obj1.push(40)
    obj1.push(50)
    obj1.push(11)
    obj1.push(130)
    obj1.push(43)
    obj1.push(10)
    obj1.push(3)
    obj1.push(17)
    obj1.display()
    print(obj1.size)
    print(obj1.pop())
    print(obj1.size)
    print(obj1.min_dict)
    obj1.get_min()
