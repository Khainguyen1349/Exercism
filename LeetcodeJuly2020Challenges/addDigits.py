import time

start = time.time()

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            return l[(num - 1) % 9]

    
inputs = 2133245
h = Solution()
print(h.addDigits(inputs))

end = time.time()
print(end - start)
        
