class Animal:
    def __init__(self,n):
        self.order=-1
        self.name=n


class Cat(Animal):
    def __init__(self,n):
        self.__init__(self,n)



class Dog(Animal):
    def __init__(self,n):
        self.__init__(self,n)
        


    

class Animal_queue:
    def __init__(self,):
        from collections import deque
        self.dog_queue=deque()
        self.cat_queue=deque()
        self.order=0

    def enqueue(self,object1):
        object1.order=self.order
        self.order+=1

        if isinstance(object1,Dog):
            self.dog_queue.append(object1)
        else:
            self.cat_queue.append(object1)

        print(self.cat_queue)
        print(self.dog_queue)

    def dequeue_any(self):
        tempdog=self.dog_queue[0].order
        tempcat=self.cat_queue[0].order
        if tempcat>tempdog:
            a=self.dog_queue.popleft()
            print(a)
        elif tempcat<tempdog:
            
        
        


    def dequeue_dog(self):
        
        


    def dequeue_dog(self):

    
    
        
