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