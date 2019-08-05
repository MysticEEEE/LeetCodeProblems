class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True