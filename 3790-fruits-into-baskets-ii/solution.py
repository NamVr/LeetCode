class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        n = len(baskets)

        for fruit in fruits:
            unset = 1
        
            for i in range(n):
        
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    unset = 0
                    break
        
            res += unset
        
        return res
