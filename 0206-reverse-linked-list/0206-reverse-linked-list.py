
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        
        # Iterate through the linked list
        while current:
            # Save the next node
            next_node = current.next
            # Reverse the direction of the pointer
            current.next = prev
            # Move to the next node
            prev = current
            current = next_node
        
        return prev
