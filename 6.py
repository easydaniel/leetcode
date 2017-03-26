class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s

        res = ''
        cycle = 2 * numRows - 2
        for row in range(0, numRows):
            for j in range(row, len(s), cycle):
                res += s[j]
                j2 = j - row + cycle - row
                if row in range(1, numRows - 1) and j2 < len(s):
                    res += s[j2]
        return res
