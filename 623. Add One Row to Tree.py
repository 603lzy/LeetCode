# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        
        curDepthStack, D, nextDepthStack = [root], 1, []
        
        while D < d - 1:
            nextDepthStack = []
            for node in curDepthStack:
                if node.left:
                    nextDepthStack.append(node.left)
                if node.right:
                    nextDepthStack.append(node.right)
            curDepthStack = nextDepthStack    
            D = D + 1
        
        for node in curDepthStack:
            if node.left:
                newLeftChild = TreeNode(v)
                newLeftChild.left = node.left
                node.left = newLeftChild
            else:
                node.left = TreeNode(v)
            if node.right:
                newRightChild = TreeNode(v)
                newRightChild.right = node.right
                node.right = newRightChild
            else:
                node.right = TreeNode(v)

        
                
        return root
        
