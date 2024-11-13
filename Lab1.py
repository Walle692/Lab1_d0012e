import random
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):  # initaliize the linked list with nothing
        self.__head = None

    def add(self, data):  # adds to the top of the single linked list
        newnode = Node(data)  # create new node with data
        if self.__head is None:  # if the linked list is empty make the new node = head
            self.__head = newnode
            return
        else:
            newnode.next = self.__head  # if the linked list was not empty make the newnode head
            self.__head = newnode  # and make the old head next in line from the new head
            return

    def removenode(self):
        if self.__head is None:  # if list is empty do nothing
            return
        else:
            self.__head = self.__head.next  # make the second node the new head
            return

    def getfirstinlist(self):  # return data of the first node in list
        if self.__head is None:
            return None
        else:
            return self.__head.data


class Stack:
    def __init__(self):  # initialize stack with an empty linked list
        self.__linkedlist = LinkedList()

    def push(self, data):  # adds object to top of stack
        self.__linkedlist.add(data)
        return

    def pop(self):  # returns the data and removes it from the stack
        data = self.__linkedlist.getfirstinlist()
        self.__linkedlist.removenode()
        return data

    def isempty(self):  # check if the list is empty
        return self.__linkedlist.getfirstinlist() is None

def createfullstack(size, topvalue): # creates a stack that is of size with values between 1 and topvalue
    stack = Stack()
    for i in range(1,size+1):
        stack.push(random.randint(1,topvalue))
    return stack

def createorderstack(size): #creates a stack that is sorted smallest to largest
    stack = Stack()
    for i in range(1,size+1):
        stack.push(i)
    return stack

def createworststack(size): #creates a stack that is sorted largest to smallest
    stack = Stack()
    for i in range(size,0,-1):
        stack.push(i)
    return stack

def sortStackLowestOnTop(stack):
    #giving reasonable names and initializeing empty stack to sort to
    unsortedStack = stack
    sortedStack = Stack()

    #checking if the unsortedstack is empty
    #if the stack is empty it returns an empty stack
    if not stack.isempty():
        highValue = stack.pop()                      #if the stack has elements get a lowValue
        if not stack.isempty():                     #check if stack is empty again if not gets a highValue
            lowValue = stack.pop()
        else:
            sortedStack.push(highValue)              #if there was only one value, return sortedStack with that value
            return sortedStack
    else:
        return sortedStack



    while  (unsortedStack.isempty() is False) and (lowValue is not None) and (highValue is not None):
        if highValue == 1 or lowValue == 1:
            print("lowvalue :"+ "highvalue :")
            print(lowValue,highValue)
        while (highValue is not None) and (lowValue is not None) and (highValue >= lowValue):             #if highValue is greater than bottom then
            sortedStack.push(highValue)             #it gets pushed into the sortedStack
            highValue = lowValue                    #the old lowValue is now high value
            if not unsortedStack.isempty():         #check if we actually can get a new value
                lowValue = unsortedStack.pop()      #get new value
            else:
                lowValue = None                     #importand to close loop

        if sortedStack.isempty():
            unsortedStack.push(highValue)
            highValue = lowValue
            if not unsortedStack.isempty():         #check if we actually can get a new value
                lowValue = unsortedStack.pop()
            else:
                lowValue = None                     #importand to close loop
        else:
            unsortedStack.push(highValue)
            if not sortedStack.isempty():
                highValue = sortedStack.pop()
            if lowValue is None:
                print(highValue,lowValue)



    if lowValue is not None:
        sortedStack.push(lowValue)
    if highValue is not None:
        sortedStack.push(highValue)

    return sortedStack

def main():
    start = createworststack(1000)
    starttime = time.time()
    result = sortStackLowestOnTop(start)
    endtime = time.time()
    runtime = endtime - starttime
    for i in range(0,1000):
        print(result.pop())
    print(runtime)



main()

