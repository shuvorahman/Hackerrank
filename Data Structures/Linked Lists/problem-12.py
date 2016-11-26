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