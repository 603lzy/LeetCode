class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.capitalize() is word or word.upper() == word or word.lower() == word # first big or all big or all small
