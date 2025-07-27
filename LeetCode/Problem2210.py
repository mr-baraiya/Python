from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Step 1: Filter out consecutive duplicates
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])
        
        count = 0
        # Step 2: Check for hill or valley in filtered list
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # Hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # Valley
        
        return count
