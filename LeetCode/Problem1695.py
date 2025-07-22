class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left, currentSum, maxSum = 0,0,0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                currentSum -= nums[left]
                left+=1
            seen.add(nums[right])
            currentSum += nums[right]

            maxSum = max(maxSum, currentSum)
        return maxSum
