from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        start = 0
        max_fruits = 0

        for end in range(len(fruits)):
            basket[fruits[end]] += 1

            # Shrink window if more than 2 fruit types
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
