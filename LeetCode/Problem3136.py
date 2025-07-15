class Solution:
    def isValid(self, word: str) -> bool:
        return ( len(word) >= 3 ) and ( word.isalnum() ) and ( any(ch.lower() in "aeiou" for ch in word) ) and ( any(ch.lower() in "bcdfghjklmnpqrstvwxyz" for ch in word ))
