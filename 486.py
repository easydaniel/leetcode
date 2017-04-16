class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0 for _ in nums]
        for i in reversed(range(len(nums))):
            for j in range(i, len(nums)):
                if i == j:
                    dp[i] = nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] >= 0
