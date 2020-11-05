import time

start = time.time()

class Solution:
    def maxPower(self, s: str) -> int:
        previousPower = 1
        currentPower = 0
        previousLetter = None
        for c in s:
            if c == previousLetter:
                currentPower = currentPower + 1
                if currentPower > previousPower:
                    previousPower = currentPower
            else:
                currentPower = 1
                previousLetter = c
        return previousPower
    
inputs = "qsgertghhgheertrrrrrzgfhgfdhfds"
h = Solution()
print(h.maxPower(inputs))

end = time.time()
print(end - start)
        
