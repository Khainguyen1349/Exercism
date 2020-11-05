import time

start = time.time()

class Solution:
    def minCostToMoveChips(self, position) -> int:
        odd = 0
        even = 0
        for i in position:
            if i%2:
                odd = odd + 1
            else:
                even = even + 1
        if odd > even:
            return even
        else:
            return odd
    
inputs = [2,2,2,3,3]
h = Solution()
print(h.minCostToMoveChips(inputs))

end = time.time()
print(end - start)
        
