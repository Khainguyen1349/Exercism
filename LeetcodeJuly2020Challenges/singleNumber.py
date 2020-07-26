import time

start = time.time()

class Solution:
    def singleNumber(self, nums):
        d = dict()
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        return [i for i in d if d[i] == 1]
    
inputs = [1,2,1,3,2,5]
h = Solution()
print(h.singleNumber(inputs))

end = time.time()
print(end - start)
        
