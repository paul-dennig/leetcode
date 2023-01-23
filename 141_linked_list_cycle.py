def hasCycle(self, head: Optional[ListNode]) -> bool:
    if (head == None):
        return False
    slow = head
    fast = head
    while (not slow.next == None) and (not fast.next == None) and (not fast.next.next == None):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            return True
    return False
