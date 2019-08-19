# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        node = root
        left = node.left
        right = node.right
        count = 0
        if node.val+ left.val == sum:
            count += 1
        elif node.val + right.val == sum:
            count += 1
        else:
            self.pathSum(left,sum)
            self.pathSum(right,sum)
        return count