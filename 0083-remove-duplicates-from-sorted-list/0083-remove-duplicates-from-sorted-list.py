class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start at the beginning of the list
        current = head
        
        # Keep going until we reach the end of the list
        while current and current.next:
            # If the current value is the same as the next value...
            if current.val == current.next.val:
                # ...skip the next node! 
                # We point 'next' to the one after the duplicate
                current.next = current.next.next
            else:
                # Otherwise, move to the next node normally
                current = current.next
                
        return head