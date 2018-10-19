# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        curLevelStack, nextLevelStack = [root], []
        if root.left is None and root.right is None:
            return [root.val]
        if root.left:
            nextLevelStack.append(root.left)
        if root.right:
            nextLevelStack.append(root.right)
        
        levelAvg = []
        
        while (nextLevelStack):
            nextLevelStack, curNodeNum, curNodeSum = [], 0, 0
            for node in curLevelStack:
                curNodeNum += 1
                curNodeSum += node.val
                if node.left:
                    nextLevelStack.append(node.left)
                if node.right:
                    nextLevelStack.append(node.right)
            levelAvg.append(float(curNodeSum)/curNodeNum)
            curLevelStack = nextLevelStack
        return levelAvg
            
