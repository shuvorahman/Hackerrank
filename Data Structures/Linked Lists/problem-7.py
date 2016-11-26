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