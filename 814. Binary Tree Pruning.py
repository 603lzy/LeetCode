# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        pruneTree()
        1. Judge whether root is none node, if is, return root
        2. Replace the left/right node of root by pruneTree(left/right)
        3. Find Whether the current node is end node, which means whether its both children are none, and if the end node value is 0, cut the end node off the tree, return None
        """
        if root is None:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.val == 0 and root.left is None and root.right is None:
            root = None
        return root
        
