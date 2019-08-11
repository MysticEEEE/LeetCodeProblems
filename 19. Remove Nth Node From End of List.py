# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        fast = dummyHead
        slow = dummyHead
        for i in range(n+1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummyHead.next

if __name__ == "__main__":
    s = Solution()
    head = ListNode([1,2,3,4,5])            
    print(s.removeNthFromEnd(head,2))
