import time
import numpy as np

start = time.time()

class Solution:
    def Function(self, nums):
        i = len(nums)-1
        L = [i]
        while i > 0:
            i = i-1
            if i+nums[i] >= L[0]:
                L = [i] + L[np.searchsorted(L,i+nums[i],side='right')-1:]
        return len(L)-1
            
        
#inputs = [2,3,1,1,4]
inputs = [2,4,5,2,1,7,2,3,4,5]
#inputs = [0]
h = Solution()
print(h.Function(inputs))

end = time.time()
print(end - start)
        
