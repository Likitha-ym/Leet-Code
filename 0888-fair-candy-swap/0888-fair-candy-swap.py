class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        target = (sum_alice + sum_bob) // 2

        set_bob = set(bobSizes)
        
        for candy in aliceSizes:
            complement_bob = target - (sum_alice - candy)
            if complement_bob in set_bob:
                return [candy, complement_bob]

solution = Solution()

aliceSizes1, bobSizes1 = [1, 1], [2, 2]
aliceSizes2, bobSizes2 = [1, 2], [2, 3]
aliceSizes3, bobSizes3 = [2], [1, 3]

print(solution.fairCandySwap(aliceSizes1, bobSizes1))  
print(solution.fairCandySwap(aliceSizes2, bobSizes2)) 
print(solution.fairCandySwap(aliceSizes3, bobSizes3)) 
