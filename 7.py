class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x *= -1
            return -int(str(x)[::-1]) if -int(str(x)[::-1]) > -(1 << 31) else 0
        return int(str(x)[::-1]) if int(str(x)[::-1]) < (1 << 31) else 0
