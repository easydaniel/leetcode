class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # sum(P) - sum(N) = S -> sum(P) = (S + sum(nums)) / 2
        total = sum(nums)
        if (S + total) & 1 or total < S:
            return 0
        target = (S + total) // 2
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[target]
        
