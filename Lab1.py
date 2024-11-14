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
    countops = 0
    #checking if the unsortedstack is empty
    #if the stack is empty it returns an empty stack
    if not stack.isempty():
        highValue = stack.pop()                     #if the stack has elements get a highvalue
        if not stack.isempty():                     #check if stack is empty again if not gets a lowvalue
            lowValue = stack.pop()
            countops += 5
        else:
            sortedStack.push(highValue)             #if there was only one value, return sortedStack with that value
            countops +=5
            return sortedStack
    else:
        countops += 1
        return sortedStack


    #main loop, runs according to conditions
    while  (unsortedStack.isempty() is False) and (lowValue is not None) and (highValue is not None):
        countops += 1

        #inner loop, the main comparison part
        while (highValue is not None) and (lowValue is not None) and (highValue >= lowValue):             #if highValue is greater than bottom then
            sortedStack.push(highValue)             #it gets pushed into the sortedStack
            highValue = lowValue                    #the old lowValue is now high value
            if not unsortedStack.isempty():         #check if we actually can get a new value
                lowValue = unsortedStack.pop()      #get new value
                countops += 4
            else:
                countops += 3
                lowValue = None                     #importand to close loop

        if sortedStack.isempty():                   #this is for when the sorted stack is empty
            unsortedStack.push(highValue)           #basically swithces position of high and lowvalue
            highValue = lowValue
            countops += 2
            if not unsortedStack.isempty():         #check if we actually can get a new value
                lowValue = unsortedStack.pop()
                countops += 2
            else:
                countops += 1
                lowValue = None                     #importand to close loop

        else:                                       #if the sortedstack has elements this runs instead
            unsortedStack.push(highValue)           #push the highvalue to unsorted
            if not sortedStack.isempty():
                highValue = sortedStack.pop()       #gets a new highvalue
                countops += 3
            if lowValue is None and unsortedStack.isempty() is False:
                lowValue = unsortedStack.pop()      #this part is for the case when the unsorted stack has elements
                countops += 2                       #this makes sure that we have both high and lowvalue, when this runs it means that we've
                                                    #come to the end of sorting, and the outerloop will close


    if highValue is not None:                       #here we add the last elements to the stack.
        sortedStack.push(highValue)
        countops += 1
    if lowValue is not None:
        sortedStack.push(lowValue)
        countops += 1

    print("this is countops " ,countops)
    return sortedStack

def newsortlowestontop(stack):
    #giving reasonable names and initializeing empty stack to sort to
    unsortedStack = stack
    sortedStack = Stack()

    #main loop, runs according to conditions, if the stack is empty it will return an empty stack
    while not unsortedStack.isempty():
        highvalue = unsortedStack.pop()             #get value for comparison

        #inner loop, the main comparison part
        while not sortedStack.isempty():

            lowvalue = sortedStack.pop()            #get value 2 for comparison

            if (highvalue > lowvalue):              #compare
                unsortedStack.push(lowvalue)        #if the highvalue was higher push the lowvalue to the unsorted stack

            else:
                sortedStack.push(lowvalue)          #if the highvalue was lower push the lowvalue to the sorted stack
                break                               #if that was the case we exit the innerloop so we can get a new highvalue

        sortedStack.push(highvalue)                 #resets the loop so when it starts again(if it does) we have the same start

    return sortedStack


def main():
    start1 = createworststack(1000)
    start2 = createworststack(2000)
    start3 = createworststack(1)
    start4 = createworststack(2)
    start5 = createworststack(3)
    start6 = createworststack(4)
    start7 = createworststack(5)
    start8 = createworststack(6)
    start9 = createworststack(7)
    hal1 = sortStackLowestOnTop(start3)
    hal2 = sortStackLowestOnTop(start4)
    hal3 = sortStackLowestOnTop(start5)
    hal4 = sortStackLowestOnTop(start6)
    hal5 = sortStackLowestOnTop(start7)
    hal6 = sortStackLowestOnTop(start8)
    hal7 = sortStackLowestOnTop(start9)
    starttime1 = time.time()
    result1 = sortStackLowestOnTop(start1)
    endtime1 = time.time()
    runtime1 = endtime1 - starttime1
    starttime2 = time.time()
    result2 = sortStackLowestOnTop(start2)
    endtime2 = time.time()
    runtime2 = endtime2 - starttime2
    #for i in range(0,1000):
    #    print(result1.pop(), result2.pop())
    print(runtime1)
    print(runtime2)



main()

