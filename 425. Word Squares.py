import itertools


def validWordSquare(words, lenw):
    """
    :type words: List[str]
    :type lenw: int
    :rtype: bool
    """
    for i in range(lenw):
        for j in range(lenw):
            if words[i][j] != words[j][i]:
                return False
    return True

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        A = [] # save the return matrix
        lenw = len(words[0])
        w = [x for x in itertools.product(words, repeat = lenw)]
        for x in w: # cannot find the repeat word
            if validWordSquare(x, lenw) == True:
                A.append(list(x))
        return A
