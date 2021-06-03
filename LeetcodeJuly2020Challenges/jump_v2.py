import time
import numpy as np

start = time.time()

class Solution:
    def Function(self, nums):
        if len(nums) == 1:
            return 0
        i = len(nums)-1
        L = [i]
        while i > 0:
            i = i-1
            if i+nums[i] > L[0]:
                if i+nums[i] > L[-1]:
                    
                k = np.searchsorted(L, i*nums[i])
                L = [i] + L[k:]
            
        
#inputs = [2,3,1,1,4]
inputs = [2,4,5,2,1,7,2,3,4,5]
#inputs = [0]
h = Solution()
print(h.Function(inputs))

end = time.time()
print(end - start)
        
