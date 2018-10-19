# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :https://discuss.leetcode.com/topic/3339/my-solution-in-python/2
        """
        if not root:
            return 0
        return 1 + max(self.minDepth(root.left), self.minDepth(root.right)) if not root.left or not root.right else 1 + min(self.minDepth(root.left), self.minDepth(root.right))
