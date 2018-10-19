class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        :https://discuss.leetcode.com/topic/3388/challenge-me-shortest-possible-answer-in-python-for-valid-palindrome-life-is-short-we-need-python
        """
        return [i.lower() for i in s if i.isalnum()] == [j.lower() for j in s[::-1] if j.isalnum()]
