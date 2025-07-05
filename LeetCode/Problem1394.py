class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # tempSet = set(arr)
        # d = {}
        # for i in tempSet:
        #     d[i] = arr.count(i)
        d = Counter(arr)
        maxCount = -1
        for i in d.keys():
            if (i == d[i]):
                maxCount = max(maxCount, d[i])
        return maxCount
