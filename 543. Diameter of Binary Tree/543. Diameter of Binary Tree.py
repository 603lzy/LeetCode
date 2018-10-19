# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        """
        :type root : TreeNode
        :rtype: int
        """
        # Base Case: Tree is empty
        if root is None:
            return 0;
        
        # If tree is not empty then height = 1+max of left/right height
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        # Get the height of left and right sub-trees
        lheight = self.getHeight(root.left)
        rheight = self.getHeight(root.right)
        
        # Get the diameter of left/right sub-trees
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        return max(lheight + rheight, ldiameter, rdiameter)
        
