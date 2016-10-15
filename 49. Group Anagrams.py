class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        :ref:http://blog.csdn.net/u010771890/article/details/52754508
        """
        A = []  # store all the words' tag, the minimum order.
        # e.g. "ate" - "aet", "tea" - "aet" 
        for s in strs:
            K = list(s)
            K.sort()
            K = "".join(K)
            A.append(K)
        
        # construct hash table
        # key: tags in A
        # value: [string with same tags]
        H = {}
        for i in xrange(len(strs)):
            if A[i] in H:
                H[A[i]].append(strs[i])
            else:
                H[A[i]] = [strs[i]]
        
        # combine the result
        M = []
        for i in H.keys():
            M.append(H[i])
        return M
        
        
        
