class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        # careless about the order
        """
        lenr = len(ransomNote)
        lenm = len(magazine)
        if lenr == 0:
            return True
        elif lenm == 0:
            return False
        else:
            magazine = list(magazine)
            cnt = 0
            for i in range(lenr):
                if ransomNote[i] in magazine:
                    cnt += 1
                    magazine.remove(ransomNote[i])    
            return cnt == lenr
                    
