import random

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
        answer = self.__linkedlist.getfirstinlist()
        if answer is None:
            return True
        else:
            return False

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

def sortstacklowestontop(stack):
    sortedstack = Stack()
    lowvalue = stack.pop()
    highvalue = stack.pop()
    while not stack.isempty():

        while highvalue > lowvalue:             #if highvalue is greater than bottom then
            sortedstack.push(highvalue)         #it gets pushed into the sortedstack
            highvalue = lowvalue                #the old lowvalue is now high value
            lowvalue = stack.pop()              #and we retrive a new lowvalue

        stack.push(highvalue)                   #when the while statement is no longer true,
        highvalue = sortedstack.pop()           #the old highvalue get pushed to the unsorded stack
                                                #and we retrive a newhighvalue, then the whileloop is tested again
    return sortedstack

def main():
    start = createorderstack(10)
    result = sortstacklowestontop(start)
    for i in range (0,10):
        print(result.pop())

main()