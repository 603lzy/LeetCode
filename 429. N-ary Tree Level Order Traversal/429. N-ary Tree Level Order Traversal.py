"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        levelOrder():
        1. If root is None, return []
        2. use two stacks to save the current level and next level nodes,
        save nodes' value of current level, then update current and next level
        3. return levelOrder
        """
        if root is None:
            return []
        stack1, stack2, levelOrderValue = [root], [], []
        while (len(stack1)):
            # for every new row
            currentLevel = []
            stack2 = []
            for i in range(len(stack1)):
                node = stack1[i]
                currentLevel.append(node.val)
                for child in node.children:
                    stack2.append(child)
            
            levelOrderValue.append(currentLevel)
            stack1 = stack2
        
        return levelOrderValue
        
