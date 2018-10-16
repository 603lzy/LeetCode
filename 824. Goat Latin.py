class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        index = 1
        goatLatinWords = []
        for word in words:
            if word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                word = word + "ma" + "a" * index
            else:
                word = word[1:] + word[0] + "ma" + "a" * index
            index = index + 1
            goatLatinWords.append(word)
        return " ".join(goatLatinWords)
                
