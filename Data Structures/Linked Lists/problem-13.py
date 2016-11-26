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
