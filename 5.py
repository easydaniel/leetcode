class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        max_len, max_start = 1, 0
        for i in range(len(s)):
            l, r = i, i
            while r < len(s) - 1 and s[r+1] == s[r]:
                r += 1
            i = r + 1
            while r < len(s) - 1 and l > 0 and s[r+1] == s[l - 1]:
                l -= 1
                r += 1
            if max_len < r - l + 1:
                max_len = r - l + 1
                max_start = l

        return s[max_start: max_start+max_len]
