class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = 0
        for  i in range(0,n):
            placed = False
            for j in range(0,n):
                if ( not used[j] ) and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
            
        return unplaced
