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
