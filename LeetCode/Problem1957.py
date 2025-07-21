from collections import Counter
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        count = 1

        for i in range(len(s)):
            # If not first character, compare with previous
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            
            # Only add if less than or equal to 2 consecutive
            if count <= 2:
                res += s[i]

        return res
