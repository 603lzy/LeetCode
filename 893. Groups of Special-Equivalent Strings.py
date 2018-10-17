class Solution:
    def isSpecialEquivRelation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
                
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        S = [[A[0]]]
        for i in range(1, len(A)):
            HASSER = 0  
            for j in range(len(S)):
                if self.isSpecialEquivRelation(S[j][0], A[i]):
                    S[j].append(A[i])
                    HASSER = 1
                    break
            if HASSER == 0:
                S.append([A[i]])
                    
        return len(S)
        
