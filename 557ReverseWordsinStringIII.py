class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "" or s == " ":
            return s
        wordsList = s.split(" ")  # words list splited by blank
        invstr = ""
        for words in wordsList:
            invstr += words[::-1]
            invstr += " "
        return invstr.strip()
