class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        Words = A.split() + B.split()
        uncommonWordsList = []
        for word in Words:
            if Words.count(word) == 1:
                uncommonWordsList.append(word)
        return uncommonWordsList
