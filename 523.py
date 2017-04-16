class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 1:
            return False
        if k < 0:
            k *= -1

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0:
                    return True
                for j in range(0, i - 1):
                    if (nums[i] - nums[j]) == 0:
                        return True
            return False

        nums = [i % k for i in nums]
        exists = {}
        for i in range(1, len(nums)):
            if nums[i] == 0:
                return True
            if (nums[i] + k) % k in exists:
                return True
            exists[nums[i - 1]] = True
        return False
            
