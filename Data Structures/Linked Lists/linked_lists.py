#!/bin/python

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""
def print_list(head):
	while head != None:
		print head.data
		head = head.next

"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head
    else:
        temp = head
        while head.next != None:
            head = head.next
        head.next = node
        return temp

"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Insert(head, data):
    node = Node(data)
    if head:
        node.next = head
    return node

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    node = Node(data)
    if position == 0:
        node.next = head
        return node
    else:
        temp = head
        for i in range(position-1):
            head = head.next
        node.next = head.next
        head.next = node
        return temp

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head:
        if position == 0:
            head = head.next
            return head
        else:
            temp = head
            for i in range(position):
                tmp, head = head, head.next
            tmp.next = head.next
            return temp

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if head:  
        if not head.next:
            print head.data
        else:
            ReversePrint(head.next)
            print head.data

  
"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head, count=0):
    if not head:
        return None
    else:
        if not head.next:
            if count==0:
                return head
            return head, head
        else:
            temp, ans = Reverse(head.next, count+1)
            temp.next = head
            count -= 1
            if count < 0:
                head.next = None
                return ans
            return head, ans
#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    if (headA == None and headB == None):
        return 1
    else:
        while(headA and headB):
            if headA.data == headB.data:
                if (headA.next == None and headB.next == None):
                    return 1
                headA, headB = headA.next, headB.next
            else:
                return 0
        return 0

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if headA == None and headB == None:
        return None
    elif headA == None and headB != None:
        return headB
    elif headA != None and headB == None:
        return headA
    else:
        if headA.data > headB.data:
            temp = headB
            headB = headA
            headA = temp
        ans = headA
        while True:
            if headA.next == None:
                headA.next = headB
                break
            elif headB == None:
                break
            else:
                if headA.next.data <= headB.data:
                    headA = headA.next
                else:
                    temp = headB.next
                    headB.next = headA.next
                    headA.next = headB
                    headB = temp
                    headA = headA.next
        return ans

"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    values = []
    if head:
        while head:
            values.append(head.data)
            head = head.next
        return values[(position*-1)-1]
    return None
  

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    visited_nodes = set()
    if head != None:
        while head.next:
            if head in visited_nodes:
                return 1
            visited_nodes.add(head)
            head = head.next
    else:
        return 0
    

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    visited_nodes = set()
    while headA or headB:
        if headA:
            if headA in visited_nodes:
                return headA.data
            else:
                visited_nodes.add(headA)
                headA = headA.next
        if headB:
            if headB in visited_nodes:
                return headB.data
            else:
                visited_nodes.add(headB)
                headB = headB.next
    return headA.data
"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    result = head
    node = Node(data)
    if not head:
        return node
    else:
        while head:
            if head.data >= node.data:
                temp = head.prev 
                head.prev = node
                node.next = head
                node.prev = temp
                temp.next = node
                return result
            else:
                if head.next:
                    head = head.next
                else:
                    head.next = node
                    node.prev = head
                    return result
  






