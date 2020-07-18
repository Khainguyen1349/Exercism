import time

start = time.time()

class Solution:
    def topKFrequent(self, nums, k: int):
        d = dict()
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        #l = sorted(d.items(), key=lambda x: x[1], reverse = False)
        return [key for (key, value) in sorted(d.items(), key=lambda x: x[1], reverse = True)][:k]

inputs = [1,6,8,3,8,9,8,4,5,3,6,4,1,5,1,3,3]   
h = Solution()
print(h.topKFrequent(inputs,3))

end = time.time()
print(end - start)
        
