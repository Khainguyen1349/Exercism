import time

start = time.time()

class Solution:
    def Function(self, nums):
        L = len(nums)-1
        print('.')
        if L<1:
            return 0
        i = 0
        step = 0
        print('.')
        while i+nums[i] < L:
            print('i = ',i)
            li = [p+nums[i+p+1] for p in range(nums[i])]
            print('max = ',max(li))
            i = i+li.index(max(li))+1
            if i==L:
                return step+1
            print('i_next = ',i)
            step = step+1
        return step+1
        
#inputs = [2,3,1,1,4]
inputs = [2,4,5,2,1,7,2,3,4,5]
#inputs = [0]
h = Solution()
print(h.Function(inputs))

end = time.time()
print(end - start)
        
