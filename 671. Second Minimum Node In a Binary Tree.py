# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        BFS
        """
        # node number 0 or 1
        if root is None or root.left is None:
            return -1
        nodeValues = []
        curLevelStack, nextLevelStack = [root], [root.left, root.right]
        while nextLevelStack:
            nextLevelStack = []
            for node in curLevelStack:
                nodeValues.append(node.val)
                if node.left:
                    nextLevelStack.append(node.left)
                    nextLevelStack.append(node.right)
            curLevelStack = nextLevelStack
        nodeValues = sorted(list(set(nodeValues)))
        if len(nodeValues) == 1:
            return -1
        else:
            return nodeValues[1]
        
