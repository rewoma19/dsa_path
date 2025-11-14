# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        # This is a placeholder node that helps us to easily start building the new merged list
        dummy = ListNode() 
        # Points to the end of the merged list. Since for now, all we have is the dummy placeholder, which would be the start and also the end of the new merged list, tail = dummy
        tail = dummy 

        # As long as list1 and list2 are not empty, run the indented code
        while list1 is not None and list2 is not None:
            # Check if the value of the list1 node is less than or equal to the value of the list2 node
            if list1.val <= list2.val:
                # if list1 is the smaller node (based on value), or has the same value as that of list2, attach list1 to the end of the merged list
                tail.next = list1 
                # move forward in list1
                list1 = list1.next 
            else:
                # if list2 is the smaller node (based on value), attach list2 to the end of the merged list
                tail.next = list2
                # move forward in list2
                list2 = list2.next

            # move the end pointer of the merged list forward
            tail = tail.next

        # if list1 is now empty, attach list2 to the end of the merged list
        if list1 is None:
            tail.next = list2
        else:
            # If not, attach list1 to the end of the merged list
            tail.next = list1

        # Recall that dummy is just a placeholder. We want to return the actual new head of the merged list
        return dummy.next
