import random
import copy
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

def createfullstack(size, topvalue):
    stack = Stack()
    for i in range(1,size+1):
        stack.push(random.randint(1,topvalue))
    return stack

def createorderstack(size):
    stack = Stack()
    for i in range(1,size+1):
        stack.push(i)
    return stack

def sortStackLowestOnTop(stack):
    unsortedStack = stack
    sortedStack = Stack()
    lowValue = stack.pop()

    print("banana",lowValue)
    highValue = stack.pop()
    print("apple", highValue)

    while unsortedStack.isempty() is False:
        print("orange")

        while (highValue is not None) and (lowValue is not None) and (highValue >= lowValue):             #if highValue is greater than bottom then
            print("grape")
            sortedStack.push(highValue)         #it gets pushed into the sortedStack
            highValue = lowValue                #the old lowValue is now high value
            lowValue = unsortedStack.pop()              #and we retrive a new lowValue
            print(lowValue, highValue)

        print("lemon")
        if sortedStack.isempty():
            unsortedStack.push(highValue)
            highValue = lowValue
            lowValue = unsortedStack.pop()
        elif unsortedStack.isempty() is False:
            unsortedStack.push(highValue)                   #when the while statement is no longer true,
            highValue = sortedStack.pop()           #the old highValue get pushed to the unsorded stack
                                                    #and we retrive a newhighValue, then the whileloop is tested again
        print(unsortedStack.isempty())

    return sortedStack

def main():
    #start = createorderstack(100)
    start = createfullstack(100,40)
    starttime = time.time()
    result = sortStackLowestOnTop(start)
    endtime = time.time()
    runtime = endtime - starttime
    print(runtime)
    for i in range(0,100):
        print(result.pop())



main()

