# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry 
            carry = sum //10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            curr.next = ListNode(carry)
        return dummyHead.next

if __name__ == "__main__":
    l1 = [2,3,4]
    l2 = [7,0,8]
    a = Solution()
    print(a.addTwoNumbers(l1,l2))


    