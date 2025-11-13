from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        prev is None because at the start, nothing comes before the first node in the list
        curr (the current node to be iterated on) is equal to the head which is the first node in the list
        '''
        prev = None
        curr = head

        # as long as the current node to be iterated on is still inside the linked list, keep on running the indented code
        while curr is not None:
            # curr.next points to the node in the list that comes after the current node.
            # It is saved in a variable next_node so that the rest of the list is not lost
            next_node = curr.next
            # As we know, curr.next normally points forward (to the node that comes after)
            # now we switch the arrow backwards (make curr.next point to the previous node, known as prev)
            curr.next = prev
            # To move through with the rest of the list, we push the prev and current node pointers forward
            prev = curr
            curr = next_node

        return prev
