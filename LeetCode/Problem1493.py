class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:  # shrink until only 1 zero remains
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # length of window minus 1 (since we must delete one element)
            max_len = max(max_len, right - left)

        return max_len
        
