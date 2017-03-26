class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        l = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                m = max(m, d[s[i]] + 1)
            d[s[i]] = i
            l = max(l, i - m + 1)
        return l
