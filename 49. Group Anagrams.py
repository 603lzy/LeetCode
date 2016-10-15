class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        A = []  # store all the words
        B = []  # store the dict 
        for s in strs:
            K = list(s)
            K.sort()
            if K not in B:  # A new word
                B.append(K)
                A.append([s])
            else: # A not is an anagrams
                A[B.index(K)].append(s)
                
        return A
        
