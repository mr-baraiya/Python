from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Step 1: Sort the nums array in ascending order
        nums.sort()

        # Step 2: Initialize `sum_` with the largest element
        sum_ = nums[-1]

        # Step 3: Initialize `prev` to track the previously added element
        prev = nums[-1]

        # Step 4: Loop from second last element to the beginning
        # Only process non-negative numbers
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < 0:
                break  # Stop if we reach a negative number

            # Step 5: If current element is not equal to previous, add to sum
            if nums[i] != prev:
                sum_ += nums[i]

            # Step 6: Update previous to current
            prev = nums[i]

        # Step 7: Return the final accumulated sum
        return sum_
