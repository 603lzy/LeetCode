# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :https://discuss.leetcode.com/topic/17540/share-my-two-python-iterative-solutions-post-order-and-modified-preorder-then-reverse
        """
        ret, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.left) # first left then right when push
                stack.append(node.right)
        return ret[::-1]
