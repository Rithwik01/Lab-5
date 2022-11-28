# -*- coding: utf-8 -*-
"""Lab 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yjmurS0jdAw9L5XSNE4cIPEzQ-vWjTEI
"""

from collections import deque

class Dequeue: #creating a class

    def __init__(self,Queue): 

        self.queue = deque()


    def enqueue(self, en: int) -> None: #method for enqueue
            self.en = en
            self.queue.append(en)     
            print(self.queue)

    def dequeue(self) -> None: #method for dequeue
        self.queue.popleft()
        print(self.queue)

    def first(self) -> int: #method to return first element in deque
        return self.queue[-1]

    def last(self) -> int: #method to return last element in deque
        return self.queue[0]


    def isEmpty(self) -> bool: #boolean to see if deque is empty
        return True if len(self.queue) == 0 else False
        print(self.queue)        
     

        
a=Dequeue(())
a.enqueue(5)
a.enqueue(3)
a.dequeue()
a.enqueue(2)
a.enqueue(8)
a.dequeue()
a.dequeue()
a.enqueue(9)
a.enqueue(1)
a.dequeue()
a.enqueue(7)
a.enqueue(6)
a.dequeue()
a.dequeue()
a.enqueue(4)
a.dequeue()
a.dequeue()

class Dequeue: #create class

    def __init__(self,Queue):

        self.queue = deque()

    def isEmpty(self) -> bool: #boolean to see if deque is empty
        return True if len(self.queue) == 0 else False
        print(self.queue)

    def addLast(self,x:int): #method to add element if the last position in deque
        self.x=x
        self.queue.append(x)
        print(self.queue)

    def addFirst(self,x:int): #method to add element if the first position in deque
        self.x=x
        self.queue.appendleft(x)
        print(self.queue)       

    def first(self, x: int): #method to return first element in deque
        self.x = x
        self.queue.append(x)
        print(self.queue)      

    def last(self,x:int): #method to return last element in deque
      self.x = x
      self.queue.appendleft(x)
      print(self.queue)

    def removeLast(self,): #method to remove last element in deque
      self.queue.popleft()
      print(self.queue)      

    def removeFirst(self): #method to remove first element in deque
      self.queue.pop()
      print(self.queue)

    def size(self): #method to see the size of deque
      print(len(self.queue))
b=Dequeue(())
b.addFirst(3)
b.addLast(8)
b.addLast(9)
b.addFirst(1)
b.isEmpty()
b.addFirst(2)
b.removeLast() 
b.addLast(7)
b.addLast(4)
b.size()
b.removeFirst()
b.removeFirst()

class Dequeue:

    def __init__(self,Queue):

        self.queue = deque()

    def isEmpty(self) -> bool: #boolean to see if deque is empty
        return True if len(self.queue) == 0 else False

    def push(self, x:int): #method to push elements in deque
        self.x=x
        self.queue.append(x)
        print(self.queue)

    def pop(self): #method to pop elements in deque
        self.queue.pop()
        print(self.queue)

c=Dequeue(())
c.push(5)
c.push(3)
c.pop()
c.push(2)
c.push(8)
c.pop()
c.pop()
c.push(9)
c.push(1)
c.pop()
c.push(7) 
c.push(6)
c.pop()
c.pop()
c.push(4)
c.pop()
c.pop()