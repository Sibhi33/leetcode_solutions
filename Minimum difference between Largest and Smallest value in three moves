class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 3:
            return 0
            
        nums.sort()
        ans = float('inf')
        
        # frist three remove
        ans = min(ans, nums[-1] - nums[3])

        # last three remove
        ans = min(ans, nums[-4] - nums[0])

        # first 2 remove, last 1 remove
        ans = min(ans, nums[-2] - nums[2])

        # first 1 remove, last 2 remove
        ans = min(ans, nums[-3] - nums[1])
        return ans
