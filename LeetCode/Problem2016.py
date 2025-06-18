class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums, reverse=True):
            return -1
        max = 0
        for i in range(0,n-1):
            for  j in range(i+1,n):
                if(nums[i] < nums[j]) and (max < (nums[j] - nums[i])):
                    max = nums[j] - nums[i]
        return max
