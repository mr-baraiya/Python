from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each number with its original index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]

        # Step 2: Sort by value descending
        top_k = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]

        # Step 3: Sort top k by original index to preserve order
        top_k.sort(key=lambda x: x[1])

        # Step 4: Extract values
        return [num for num, _ in top_k]
