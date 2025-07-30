class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAnd = max(nums)
        maxLen , currentLen = 0, 0
        for num in nums:
            if ( num == maxAnd ):
                currentLen += 1
                maxLen = max(maxLen, currentLen)
            else:
                currentLen = 0
        return maxLen
        
