from collections import Counter

class Solution:
    def possibleStringCount(self, word: str) -> int:
        # x = Counter(word)
        # count = 1
        # for i in x.keys():
        #     if (x[i] > 1):
        #         count += x[i]-1
        # return count
        if (len(word) == 1):
            return 1
        count = 1
        for i in range(len(word)-1):
            if(word[i] == word[i+1]):
                count+=1
        return count
