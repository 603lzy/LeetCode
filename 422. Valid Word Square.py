class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        lenw = len(words)
        try:
            for i in range(lenw):
                lenj = len(words[i])
                for j in range(lenj):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except IndexError:
            return False
