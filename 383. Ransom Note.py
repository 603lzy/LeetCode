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
            for i in ransomNote:
                if i in magazine:
                    magazine.remove(i)    
            return (len(magazine) + lenr) == lenm
                    
