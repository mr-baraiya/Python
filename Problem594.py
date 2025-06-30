class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = Counter(nums)
        print(count)
        maxLength = 0
        for num in count:
            if num + 1 in count:
                maxLength = max(maxLength, count[num] + count[num + 1])
        return maxLength
