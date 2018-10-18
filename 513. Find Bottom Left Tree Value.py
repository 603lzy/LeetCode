# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curLevelStack, nextLevelStack = [root], []
        if root.left:
            nextLevelStack.append(root.left)
        if root.right:
            nextLevelStack.append(root.right)
        
        while (nextLevelStack):
            curLevelStack, nextLevelStack = nextLevelStack, []
            for node in curLevelStack:
                if node.left:
                    nextLevelStack.append(node.left)
                if node.right:
                    nextLevelStack.append(node.right)
        return curLevelStack[0].val
            
        
