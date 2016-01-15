class queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.start_flag=0

    def push(self,d):
        if self.start_flag==0:
            self.start_flag=1
            self.stack1.append(d)
            return True
        if len(self.stack1)>0:
            self.stack1.append(d)
        elif len(self.stack2)>0:
            while len(self.stack2)>0:
                temp=self.stack2.pop()
                if len(self.stack2)==0:
                    break
                stack1.append(temp)
            stack1.append(d)
            
        

    def pop1(self):
        if len(self.stack1)>0:   
            while len(self.stack1)>0:
                temp=self.stack1.pop()
                self.stack2.append(temp)
                if len(self.stack1)==0:
                    break

            final_pop_element=self.stack2.pop()
            print(final_pop_element)

        elif len(self.stack2)>0:
            temp=selfstack2.pop()
            print(temp)
            


    def peek(self):
        if len(self.stack2)>0:
            temp=self.stack2[len(stack2)-1]
            print(temp)
        elif len(self.stack1)>0:
            while len(self.stack1)>0:
                temp=self.stack1.pop()
                self.stack2.append(temp)
                if len(self.stack1)==0:
                    break
            final_peek_element=self.stack2[len(self.stack2)-1]
            print(final_peek_element)

    def display(self):
        print("stack1   ",end="")
        print(self.stack1)
        print("stack2   ",end="")
        print(self.stack2)

if __name__=="__main__":
    obj1=queue()
    obj1.push(1)
    obj1.push(2)
    obj1.push(3)
    obj1.push(4)
    obj1.push(5)
    obj1.display()

    obj1.pop1()
    obj1.display()    








                
                
        
        
