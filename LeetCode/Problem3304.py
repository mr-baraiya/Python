class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        
        while len(word) <= k:
            res = [chr((ord(ch) - ord('a') + 1) % 26 + ord('a')) for ch in word]
            word += ''.join(res)
        
        return word[k-1]
