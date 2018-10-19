class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        try:
            for i in range(len(words)):
                for j in range(len(words[j])):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except IndexError:
            return False
