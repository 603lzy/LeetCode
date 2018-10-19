# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        :https://discuss.leetcode.com/topic/9064/73ms-8-line-python-code-for-path-sum-with-comments/5
        """
        try:
            target -= root.val
            return not target if not root.left and not root.right else Solution().hasPathSum(root.left, target) or Solution().hasPathSum(root.right, target)
        except AttributeError:
            return False
