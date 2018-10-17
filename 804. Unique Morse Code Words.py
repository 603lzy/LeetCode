class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = string.ascii_lowercase
        dictMorseCode = {}
        MorseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        wordsMorse = []
        for i in range(26):
            dictMorseCode[alphabet[i]] = MorseCode[i]
        for word in words:      # for each word in wordslist
            s = ""              # current word morse code
            for c in word:      # for each letter in the word
                s = s + dictMorseCode[c]
            wordsMorse.append(s)
        return len(set(wordsMorse))
            
