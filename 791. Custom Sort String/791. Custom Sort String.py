class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dictR = {}      # a-z: T.count(a-z)
        R = ""          # return str
        for character in string.ascii_lowercase[:27]:
            dictR[character] = T.count(character) # dictR[a-z]:T.count(a-z)
        
        for character in S:
            R = R + character * dictR[character]
            dictR.pop(character)
            
        for character in dictR:
            R = R + character * dictR[character]
            
        return R
                
