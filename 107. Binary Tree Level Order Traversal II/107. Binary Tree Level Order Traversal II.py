# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # check root = NULL
        if root is None:
            return []
        # check root.left and root.right = NULL
        if root.left:
            nextLevelStack = [root.left]
        elif root.right:
            nextLevelStack = [root.right]
        else:
            return [[root.val]]
        
        curLevelStack, levelOrderBottom = [root], []
        while nextLevelStack:
            nextLevelStack, curLevelValue = [], []
            for node in curLevelStack:
                curLevelValue.append(node.val)
                if node.left:
                    nextLevelStack.append(node.left)
                if node.right:
                    nextLevelStack.append(node.right)
            curLevelStack = nextLevelStack
            levelOrderBottom.insert(0, curLevelValue)
        return levelOrderBottom
