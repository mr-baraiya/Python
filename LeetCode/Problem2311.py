class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                count += 1
                power += 1
            else:
                if (1 << power) <= k - value:
                    value += (1 << power)
                    count += 1
                    power += 1
                else:
                    power += 1
        return count
