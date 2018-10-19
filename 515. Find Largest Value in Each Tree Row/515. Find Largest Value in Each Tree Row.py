# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        
        curLevelStack, nextLevelStack = [root], [root]
        maxValues = []
        while nextLevelStack:
            nextLevelStack = []
            curLevelValues = []
            for node in curLevelStack:
                curLevelValues.append(node.val)
                if node.left:
                    nextLevelStack.append(node.left)
                if node.right:
                    nextLevelStack.append(node.right)
            maxValues.append(max(curLevelValues))
            curLevelStack = nextLevelStack
        return maxValues
