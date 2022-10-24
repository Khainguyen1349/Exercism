import time

start = time.time()

class Solution:
    def permuteUnique(self,nums):
        L = [[nums[0]]]
        for i in range(len(nums)-1):
            L_temp = []
            for j in range(len(L)):
                for k in range(i+2):
                    L1_temp = L[j].copy()
                    L1_temp.insert(k,nums[i+1])
##                    print(L1_temp)
                    L_temp.append(L1_temp)
##                    print(L_temp)
            L = L_temp
            print(L)
        return [list(i) for i in {tuple(j) for j in L}]
    
input1 = [1,2,3,4,5]
input2 = [-1,2,-1,2,1,-1,2,1]

#test = [[-1,-1,-1,1,1,2,2,2],[-1,-1,-1,1,2,1,2,2],[-1,-1,-1,1,2,2,1,2],[-1,-1,-1,1,2,2,2,1],[-1,-1,-1,2,1,1,2,2],[-1,-1,-1,2,1,2,1,2],[-1,-1,-1,2,1,2,2,1],[-1,-1,-1,2,2,1,1,2],[-1,-1,-1,2,2,1,2,1],[-1,-1,-1,2,2,2,1,1],[-1,-1,1,-1,1,2,2,2],[-1,-1,1,-1,2,1,2,2],[-1,-1,1,-1,2,2,1,2],[-1,-1,1,-1,2,2,2,1],[-1,-1,1,1,-1,2,2,2],[-1,-1,1,1,2,-1,2,2],[-1,-1,1,1,2,2,-1,2],[-1,-1,1,1,2,2,2,-1],[-1,-1,1,2,-1,1,2,2],[-1,-1,1,2,-1,2,1,2],[-1,-1,1,2,-1,2,2,1],[-1,-1,1,2,1,-1,2,2],[-1,-1,1,2,1,2,-1,2],[-1,-1,1,2,1,2,2,-1],[-1,-1,1,2,2,-1,1,2],[-1,-1,1,2,2,-1,2,1],[-1,-1,1,2,2,1,-1,2],[-1,-1,1,2,2,1,2,-1],[-1,-1,1,2,2,2,-1,1],[-1,-1,1,2,2,2,1,-1],[-1,-1,2,-1,1,1,2,2],[-1,-1,2,-1,1,2,1,2],[-1,-1,2,-1,1,2,2,1],[-1,-1,2,-1,2,1,1,2],[-1,-1,2,-1,2,1,2,1],[-1,-1,2,-1,2,2,1,1],[-1,-1,2,1,-1,1,2,2],[-1,-1,2,1,-1,2,1,2],[-1,-1,2,1,-1,2,2,1],[-1,-1,2,1,1,-1,2,2],[-1,-1,2,1,1,2,-1,2],[-1,-1,2,1,1,2,2,-1],[-1,-1,2,1,2,-1,1,2],[-1,-1,2,1,2,-1,2,1],[-1,-1,2,1,2,1,-1,2],[-1,-1,2,1,2,1,2,-1],[-1,-1,2,1,2,2,-1,1],[-1,-1,2,1,2,2,1,-1],[-1,-1,2,2,-1,1,1,2],[-1,-1,2,2,-1,1,2,1],[-1,-1,2,2,-1,2,1,1],[-1,-1,2,2,1,-1,1,2],[-1,-1,2,2,1,-1,2,1],[-1,-1,2,2,1,1,-1,2],[-1,-1,2,2,1,1,2,-1],[-1,-1,2,2,1,2,-1,1],[-1,-1,2,2,1,2,1,-1],[-1,-1,2,2,2,-1,1,1],[-1,-1,2,2,2,1,-1,1],[-1,-1,2,2,2,1,1,-1],[-1,1,-1,-1,1,2,2,2],[-1,1,-1,-1,2,1,2,2],[-1,1,-1,-1,2,2,1,2],[-1,1,-1,-1,2,2,2,1],[-1,1,-1,1,-1,2,2,2],[-1,1,-1,1,2,-1,2,2],[-1,1,-1,1,2,2,-1,2],[-1,1,-1,1,2,2,2,-1],[-1,1,-1,2,-1,1,2,2],[-1,1,-1,2,-1,2,1,2],[-1,1,-1,2,-1,2,2,1],[-1,1,-1,2,1,-1,2,2],[-1,1,-1,2,1,2,-1,2],[-1,1,-1,2,1,2,2,-1],[-1,1,-1,2,2,-1,1,2],[-1,1,-1,2,2,-1,2,1],[-1,1,-1,2,2,1,-1,2],[-1,1,-1,2,2,1,2,-1],[-1,1,-1,2,2,2,-1,1],[-1,1,-1,2,2,2,1,-1],[-1,1,1,-1,-1,2,2,2],[-1,1,1,-1,2,-1,2,2],[-1,1,1,-1,2,2,-1,2],[-1,1,1,-1,2,2,2,-1],[-1,1,1,2,-1,-1,2,2],[-1,1,1,2,-1,2,-1,2],[-1,1,1,2,-1,2,2,-1],[-1,1,1,2,2,-1,-1,2],[-1,1,1,2,2,-1,2,-1],[-1,1,1,2,2,2,-1,-1],[-1,1,2,-1,-1,1,2,2],[-1,1,2,-1,-1,2,1,2],[-1,1,2,-1,-1,2,2,1],[-1,1,2,-1,1,-1,2,2],[-1,1,2,-1,1,2,-1,2],[-1,1,2,-1,1,2,2,-1],[-1,1,2,-1,2,-1,1,2],[-1,1,2,-1,2,-1,2,1],[-1,1,2,-1,2,1,-1,2],[-1,1,2,-1,2,1,2,-1],[-1,1,2,-1,2,2,-1,1],[-1,1,2,-1,2,2,1,-1],[-1,1,2,1,-1,-1,2,2],[-1,1,2,1,-1,2,-1,2],[-1,1,2,1,-1,2,2,-1],[-1,1,2,1,2,-1,-1,2],[-1,1,2,1,2,-1,2,-1],[-1,1,2,1,2,2,-1,-1],[-1,1,2,2,-1,-1,1,2],[-1,1,2,2,-1,-1,2,1],[-1,1,2,2,-1,1,-1,2],[-1,1,2,2,-1,1,2,-1],[-1,1,2,2,-1,2,-1,1],[-1,1,2,2,-1,2,1,-1],[-1,1,2,2,1,-1,-1,2],[-1,1,2,2,1,-1,2,-1],[-1,1,2,2,1,2,-1,-1],[-1,1,2,2,2,-1,-1,1],[-1,1,2,2,2,-1,1,-1],[-1,1,2,2,2,1,-1,-1],[-1,2,-1,-1,1,1,2,2],[-1,2,-1,-1,1,2,1,2],[-1,2,-1,-1,1,2,2,1],[-1,2,-1,-1,2,1,1,2],[-1,2,-1,-1,2,1,2,1],[-1,2,-1,-1,2,2,1,1],[-1,2,-1,1,-1,1,2,2],[-1,2,-1,1,-1,2,1,2],[-1,2,-1,1,-1,2,2,1],[-1,2,-1,1,1,-1,2,2],[-1,2,-1,1,1,2,-1,2],[-1,2,-1,1,1,2,2,-1],[-1,2,-1,1,2,-1,1,2],[-1,2,-1,1,2,-1,2,1],[-1,2,-1,1,2,1,-1,2],[-1,2,-1,1,2,1,2,-1],[-1,2,-1,1,2,2,-1,1],[-1,2,-1,1,2,2,1,-1],[-1,2,-1,2,-1,1,1,2],[-1,2,-1,2,-1,1,2,1],[-1,2,-1,2,-1,2,1,1],[-1,2,-1,2,1,-1,1,2],[-1,2,-1,2,1,-1,2,1],[-1,2,-1,2,1,1,-1,2],[-1,2,-1,2,1,1,2,-1],[-1,2,-1,2,1,2,-1,1],[-1,2,-1,2,1,2,1,-1],[-1,2,-1,2,2,-1,1,1],[-1,2,-1,2,2,1,-1,1],[-1,2,-1,2,2,1,1,-1],[-1,2,1,-1,-1,1,2,2],[-1,2,1,-1,-1,2,1,2],[-1,2,1,-1,-1,2,2,1],[-1,2,1,-1,1,-1,2,2],[-1,2,1,-1,1,2,-1,2],[-1,2,1,-1,1,2,2,-1],[-1,2,1,-1,2,-1,1,2],[-1,2,1,-1,2,-1,2,1],[-1,2,1,-1,2,1,-1,2],[-1,2,1,-1,2,1,2,-1],[-1,2,1,-1,2,2,-1,1],[-1,2,1,-1,2,2,1,-1],[-1,2,1,1,-1,-1,2,2],[-1,2,1,1,-1,2,-1,2],[-1,2,1,1,-1,2,2,-1],[-1,2,1,1,2,-1,-1,2],[-1,2,1,1,2,-1,2,-1],[-1,2,1,1,2,2,-1,-1],[-1,2,1,2,-1,-1,1,2],[-1,2,1,2,-1,-1,2,1],[-1,2,1,2,-1,1,-1,2],[-1,2,1,2,-1,1,2,-1],[-1,2,1,2,-1,2,-1,1],[-1,2,1,2,-1,2,1,-1],[-1,2,1,2,1,-1,-1,2],[-1,2,1,2,1,-1,2,-1],[-1,2,1,2,1,2,-1,-1],[-1,2,1,2,2,-1,-1,1],[-1,2,1,2,2,-1,1,-1],[-1,2,1,2,2,1,-1,-1],[-1,2,2,-1,-1,1,1,2],[-1,2,2,-1,-1,1,2,1],[-1,2,2,-1,-1,2,1,1],[-1,2,2,-1,1,-1,1,2],[-1,2,2,-1,1,-1,2,1],[-1,2,2,-1,1,1,-1,2],[-1,2,2,-1,1,1,2,-1],[-1,2,2,-1,1,2,-1,1],[-1,2,2,-1,1,2,1,-1],[-1,2,2,-1,2,-1,1,1],[-1,2,2,-1,2,1,-1,1],[-1,2,2,-1,2,1,1,-1],[-1,2,2,1,-1,-1,1,2],[-1,2,2,1,-1,-1,2,1],[-1,2,2,1,-1,1,-1,2],[-1,2,2,1,-1,1,2,-1],[-1,2,2,1,-1,2,-1,1],[-1,2,2,1,-1,2,1,-1],[-1,2,2,1,1,-1,-1,2],[-1,2,2,1,1,-1,2,-1],[-1,2,2,1,1,2,-1,-1],[-1,2,2,1,2,-1,-1,1],[-1,2,2,1,2,-1,1,-1],[-1,2,2,1,2,1,-1,-1],[-1,2,2,2,-1,-1,1,1],[-1,2,2,2,-1,1,-1,1],[-1,2,2,2,-1,1,1,-1],[-1,2,2,2,1,-1,-1,1],[-1,2,2,2,1,-1,1,-1],[-1,2,2,2,1,1,-1,-1],[1,-1,-1,-1,1,2,2,2],[1,-1,-1,-1,2,1,2,2],[1,-1,-1,-1,2,2,1,2],[1,-1,-1,-1,2,2,2,1],[1,-1,-1,1,-1,2,2,2],[1,-1,-1,1,2,-1,2,2],[1,-1,-1,1,2,2,-1,2],[1,-1,-1,1,2,2,2,-1],[1,-1,-1,2,-1,1,2,2],[1,-1,-1,2,-1,2,1,2],[1,-1,-1,2,-1,2,2,1],[1,-1,-1,2,1,-1,2,2],[1,-1,-1,2,1,2,-1,2],[1,-1,-1,2,1,2,2,-1],[1,-1,-1,2,2,-1,1,2],[1,-1,-1,2,2,-1,2,1],[1,-1,-1,2,2,1,-1,2],[1,-1,-1,2,2,1,2,-1],[1,-1,-1,2,2,2,-1,1],[1,-1,-1,2,2,2,1,-1],[1,-1,1,-1,-1,2,2,2],[1,-1,1,-1,2,-1,2,2],[1,-1,1,-1,2,2,-1,2],[1,-1,1,-1,2,2,2,-1],[1,-1,1,2,-1,-1,2,2],[1,-1,1,2,-1,2,-1,2],[1,-1,1,2,-1,2,2,-1],[1,-1,1,2,2,-1,-1,2],[1,-1,1,2,2,-1,2,-1],[1,-1,1,2,2,2,-1,-1],[1,-1,2,-1,-1,1,2,2],[1,-1,2,-1,-1,2,1,2],[1,-1,2,-1,-1,2,2,1],[1,-1,2,-1,1,-1,2,2],[1,-1,2,-1,1,2,-1,2],[1,-1,2,-1,1,2,2,-1],[1,-1,2,-1,2,-1,1,2],[1,-1,2,-1,2,-1,2,1],[1,-1,2,-1,2,1,-1,2],[1,-1,2,-1,2,1,2,-1],[1,-1,2,-1,2,2,-1,1],[1,-1,2,-1,2,2,1,-1],[1,-1,2,1,-1,-1,2,2],[1,-1,2,1,-1,2,-1,2],[1,-1,2,1,-1,2,2,-1],[1,-1,2,1,2,-1,-1,2],[1,-1,2,1,2,-1,2,-1],[1,-1,2,1,2,2,-1,-1],[1,-1,2,2,-1,-1,1,2],[1,-1,2,2,-1,-1,2,1],[1,-1,2,2,-1,1,-1,2],[1,-1,2,2,-1,1,2,-1],[1,-1,2,2,-1,2,-1,1],[1,-1,2,2,-1,2,1,-1],[1,-1,2,2,1,-1,-1,2],[1,-1,2,2,1,-1,2,-1],[1,-1,2,2,1,2,-1,-1],[1,-1,2,2,2,-1,-1,1],[1,-1,2,2,2,-1,1,-1],[1,-1,2,2,2,1,-1,-1],[1,1,-1,-1,-1,2,2,2],[1,1,-1,-1,2,-1,2,2],[1,1,-1,-1,2,2,-1,2],[1,1,-1,-1,2,2,2,-1],[1,1,-1,2,-1,-1,2,2],[1,1,-1,2,-1,2,-1,2],[1,1,-1,2,-1,2,2,-1],[1,1,-1,2,2,-1,-1,2],[1,1,-1,2,2,-1,2,-1],[1,1,-1,2,2,2,-1,-1],[1,1,2,-1,-1,-1,2,2],[1,1,2,-1,-1,2,-1,2],[1,1,2,-1,-1,2,2,-1],[1,1,2,-1,2,-1,-1,2],[1,1,2,-1,2,-1,2,-1],[1,1,2,-1,2,2,-1,-1],[1,1,2,2,-1,-1,-1,2],[1,1,2,2,-1,-1,2,-1],[1,1,2,2,-1,2,-1,-1],[1,1,2,2,2,-1,-1,-1],[1,2,-1,-1,-1,1,2,2],[1,2,-1,-1,-1,2,1,2],[1,2,-1,-1,-1,2,2,1],[1,2,-1,-1,1,-1,2,2],[1,2,-1,-1,1,2,-1,2],[1,2,-1,-1,1,2,2,-1],[1,2,-1,-1,2,-1,1,2],[1,2,-1,-1,2,-1,2,1],[1,2,-1,-1,2,1,-1,2],[1,2,-1,-1,2,1,2,-1],[1,2,-1,-1,2,2,-1,1],[1,2,-1,-1,2,2,1,-1],[1,2,-1,1,-1,-1,2,2],[1,2,-1,1,-1,2,-1,2],[1,2,-1,1,-1,2,2,-1],[1,2,-1,1,2,-1,-1,2],[1,2,-1,1,2,-1,2,-1],[1,2,-1,1,2,2,-1,-1],[1,2,-1,2,-1,-1,1,2],[1,2,-1,2,-1,-1,2,1],[1,2,-1,2,-1,1,-1,2],[1,2,-1,2,-1,1,2,-1],[1,2,-1,2,-1,2,-1,1],[1,2,-1,2,-1,2,1,-1],[1,2,-1,2,1,-1,-1,2],[1,2,-1,2,1,-1,2,-1],[1,2,-1,2,1,2,-1,-1],[1,2,-1,2,2,-1,-1,1],[1,2,-1,2,2,-1,1,-1],[1,2,-1,2,2,1,-1,-1],[1,2,1,-1,-1,-1,2,2],[1,2,1,-1,-1,2,-1,2],[1,2,1,-1,-1,2,2,-1],[1,2,1,-1,2,-1,-1,2],[1,2,1,-1,2,-1,2,-1],[1,2,1,-1,2,2,-1,-1],[1,2,1,2,-1,-1,-1,2],[1,2,1,2,-1,-1,2,-1],[1,2,1,2,-1,2,-1,-1],[1,2,1,2,2,-1,-1,-1],[1,2,2,-1,-1,-1,1,2],[1,2,2,-1,-1,-1,2,1],[1,2,2,-1,-1,1,-1,2],[1,2,2,-1,-1,1,2,-1],[1,2,2,-1,-1,2,-1,1],[1,2,2,-1,-1,2,1,-1],[1,2,2,-1,1,-1,-1,2],[1,2,2,-1,1,-1,2,-1],[1,2,2,-1,1,2,-1,-1],[1,2,2,-1,2,-1,-1,1],[1,2,2,-1,2,-1,1,-1],[1,2,2,-1,2,1,-1,-1],[1,2,2,1,-1,-1,-1,2],[1,2,2,1,-1,-1,2,-1],[1,2,2,1,-1,2,-1,-1],[1,2,2,1,2,-1,-1,-1],[1,2,2,2,-1,-1,-1,1],[1,2,2,2,-1,-1,1,-1],[1,2,2,2,-1,1,-1,-1],[1,2,2,2,1,-1,-1,-1],[2,-1,-1,-1,1,1,2,2],[2,-1,-1,-1,1,2,1,2],[2,-1,-1,-1,1,2,2,1],[2,-1,-1,-1,2,1,1,2],[2,-1,-1,-1,2,1,2,1],[2,-1,-1,-1,2,2,1,1],[2,-1,-1,1,-1,1,2,2],[2,-1,-1,1,-1,2,1,2],[2,-1,-1,1,-1,2,2,1],[2,-1,-1,1,1,-1,2,2],[2,-1,-1,1,1,2,-1,2],[2,-1,-1,1,1,2,2,-1],[2,-1,-1,1,2,-1,1,2],[2,-1,-1,1,2,-1,2,1],[2,-1,-1,1,2,1,-1,2],[2,-1,-1,1,2,1,2,-1],[2,-1,-1,1,2,2,-1,1],[2,-1,-1,1,2,2,1,-1],[2,-1,-1,2,-1,1,1,2],[2,-1,-1,2,-1,1,2,1],[2,-1,-1,2,-1,2,1,1],[2,-1,-1,2,1,-1,1,2],[2,-1,-1,2,1,-1,2,1],[2,-1,-1,2,1,1,-1,2],[2,-1,-1,2,1,1,2,-1],[2,-1,-1,2,1,2,-1,1],[2,-1,-1,2,1,2,1,-1],[2,-1,-1,2,2,-1,1,1],[2,-1,-1,2,2,1,-1,1],[2,-1,-1,2,2,1,1,-1],[2,-1,1,-1,-1,1,2,2],[2,-1,1,-1,-1,2,1,2],[2,-1,1,-1,-1,2,2,1],[2,-1,1,-1,1,-1,2,2],[2,-1,1,-1,1,2,-1,2],[2,-1,1,-1,1,2,2,-1],[2,-1,1,-1,2,-1,1,2],[2,-1,1,-1,2,-1,2,1],[2,-1,1,-1,2,1,-1,2],[2,-1,1,-1,2,1,2,-1],[2,-1,1,-1,2,2,-1,1],[2,-1,1,-1,2,2,1,-1],[2,-1,1,1,-1,-1,2,2],[2,-1,1,1,-1,2,-1,2],[2,-1,1,1,-1,2,2,-1],[2,-1,1,1,2,-1,-1,2],[2,-1,1,1,2,-1,2,-1],[2,-1,1,1,2,2,-1,-1],[2,-1,1,2,-1,-1,1,2],[2,-1,1,2,-1,-1,2,1],[2,-1,1,2,-1,1,-1,2],[2,-1,1,2,-1,1,2,-1],[2,-1,1,2,-1,2,-1,1],[2,-1,1,2,-1,2,1,-1],[2,-1,1,2,1,-1,-1,2],[2,-1,1,2,1,-1,2,-1],[2,-1,1,2,1,2,-1,-1],[2,-1,1,2,2,-1,-1,1],[2,-1,1,2,2,-1,1,-1],[2,-1,1,2,2,1,-1,-1],[2,-1,2,-1,-1,1,1,2],[2,-1,2,-1,-1,1,2,1],[2,-1,2,-1,-1,2,1,1],[2,-1,2,-1,1,-1,1,2],[2,-1,2,-1,1,-1,2,1],[2,-1,2,-1,1,1,-1,2],[2,-1,2,-1,1,1,2,-1],[2,-1,2,-1,1,2,-1,1],[2,-1,2,-1,1,2,1,-1],[2,-1,2,-1,2,-1,1,1],[2,-1,2,-1,2,1,-1,1],[2,-1,2,-1,2,1,1,-1],[2,-1,2,1,-1,-1,1,2],[2,-1,2,1,-1,-1,2,1],[2,-1,2,1,-1,1,-1,2],[2,-1,2,1,-1,1,2,-1],[2,-1,2,1,-1,2,-1,1],[2,-1,2,1,-1,2,1,-1],[2,-1,2,1,1,-1,-1,2],[2,-1,2,1,1,-1,2,-1],[2,-1,2,1,1,2,-1,-1],[2,-1,2,1,2,-1,-1,1],[2,-1,2,1,2,-1,1,-1],[2,-1,2,1,2,1,-1,-1],[2,-1,2,2,-1,-1,1,1],[2,-1,2,2,-1,1,-1,1],[2,-1,2,2,-1,1,1,-1],[2,-1,2,2,1,-1,-1,1],[2,-1,2,2,1,-1,1,-1],[2,-1,2,2,1,1,-1,-1],[2,1,-1,-1,-1,1,2,2],[2,1,-1,-1,-1,2,1,2],[2,1,-1,-1,-1,2,2,1],[2,1,-1,-1,1,-1,2,2],[2,1,-1,-1,1,2,-1,2],[2,1,-1,-1,1,2,2,-1],[2,1,-1,-1,2,-1,1,2],[2,1,-1,-1,2,-1,2,1],[2,1,-1,-1,2,1,-1,2],[2,1,-1,-1,2,1,2,-1],[2,1,-1,-1,2,2,-1,1],[2,1,-1,-1,2,2,1,-1],[2,1,-1,1,-1,-1,2,2],[2,1,-1,1,-1,2,-1,2],[2,1,-1,1,-1,2,2,-1],[2,1,-1,1,2,-1,-1,2],[2,1,-1,1,2,-1,2,-1],[2,1,-1,1,2,2,-1,-1],[2,1,-1,2,-1,-1,1,2],[2,1,-1,2,-1,-1,2,1],[2,1,-1,2,-1,1,-1,2],[2,1,-1,2,-1,1,2,-1],[2,1,-1,2,-1,2,-1,1],[2,1,-1,2,-1,2,1,-1],[2,1,-1,2,1,-1,-1,2],[2,1,-1,2,1,-1,2,-1],[2,1,-1,2,1,2,-1,-1],[2,1,-1,2,2,-1,-1,1],[2,1,-1,2,2,-1,1,-1],[2,1,-1,2,2,1,-1,-1],[2,1,1,-1,-1,-1,2,2],[2,1,1,-1,-1,2,-1,2],[2,1,1,-1,-1,2,2,-1],[2,1,1,-1,2,-1,-1,2],[2,1,1,-1,2,-1,2,-1],[2,1,1,-1,2,2,-1,-1],[2,1,1,2,-1,-1,-1,2],[2,1,1,2,-1,-1,2,-1],[2,1,1,2,-1,2,-1,-1],[2,1,1,2,2,-1,-1,-1],[2,1,2,-1,-1,-1,1,2],[2,1,2,-1,-1,-1,2,1],[2,1,2,-1,-1,1,-1,2],[2,1,2,-1,-1,1,2,-1],[2,1,2,-1,-1,2,-1,1],[2,1,2,-1,-1,2,1,-1],[2,1,2,-1,1,-1,-1,2],[2,1,2,-1,1,-1,2,-1],[2,1,2,-1,1,2,-1,-1],[2,1,2,-1,2,-1,-1,1],[2,1,2,-1,2,-1,1,-1],[2,1,2,-1,2,1,-1,-1],[2,1,2,1,-1,-1,-1,2],[2,1,2,1,-1,-1,2,-1],[2,1,2,1,-1,2,-1,-1],[2,1,2,1,2,-1,-1,-1],[2,1,2,2,-1,-1,-1,1],[2,1,2,2,-1,-1,1,-1],[2,1,2,2,-1,1,-1,-1],[2,1,2,2,1,-1,-1,-1],[2,2,-1,-1,-1,1,1,2],[2,2,-1,-1,-1,1,2,1],[2,2,-1,-1,-1,2,1,1],[2,2,-1,-1,1,-1,1,2],[2,2,-1,-1,1,-1,2,1],[2,2,-1,-1,1,1,-1,2],[2,2,-1,-1,1,1,2,-1],[2,2,-1,-1,1,2,-1,1],[2,2,-1,-1,1,2,1,-1],[2,2,-1,-1,2,-1,1,1],[2,2,-1,-1,2,1,-1,1],[2,2,-1,-1,2,1,1,-1],[2,2,-1,1,-1,-1,1,2],[2,2,-1,1,-1,-1,2,1],[2,2,-1,1,-1,1,-1,2],[2,2,-1,1,-1,1,2,-1],[2,2,-1,1,-1,2,-1,1],[2,2,-1,1,-1,2,1,-1],[2,2,-1,1,1,-1,-1,2],[2,2,-1,1,1,-1,2,-1],[2,2,-1,1,1,2,-1,-1],[2,2,-1,1,2,-1,-1,1],[2,2,-1,1,2,-1,1,-1],[2,2,-1,1,2,1,-1,-1],[2,2,-1,2,-1,-1,1,1],[2,2,-1,2,-1,1,-1,1],[2,2,-1,2,-1,1,1,-1],[2,2,-1,2,1,-1,-1,1],[2,2,-1,2,1,-1,1,-1],[2,2,-1,2,1,1,-1,-1],[2,2,1,-1,-1,-1,1,2],[2,2,1,-1,-1,-1,2,1],[2,2,1,-1,-1,1,-1,2],[2,2,1,-1,-1,1,2,-1],[2,2,1,-1,-1,2,-1,1],[2,2,1,-1,-1,2,1,-1],[2,2,1,-1,1,-1,-1,2],[2,2,1,-1,1,-1,2,-1],[2,2,1,-1,1,2,-1,-1],[2,2,1,-1,2,-1,-1,1],[2,2,1,-1,2,-1,1,-1],[2,2,1,-1,2,1,-1,-1],[2,2,1,1,-1,-1,-1,2],[2,2,1,1,-1,-1,2,-1],[2,2,1,1,-1,2,-1,-1],[2,2,1,1,2,-1,-1,-1],[2,2,1,2,-1,-1,-1,1],[2,2,1,2,-1,-1,1,-1],[2,2,1,2,-1,1,-1,-1],[2,2,1,2,1,-1,-1,-1],[2,2,2,-1,-1,-1,1,1],[2,2,2,-1,-1,1,-1,1],[2,2,2,-1,-1,1,1,-1],[2,2,2,-1,1,-1,-1,1],[2,2,2,-1,1,-1,1,-1],[2,2,2,-1,1,1,-1,-1],[2,2,2,1,-1,-1,-1,1],[2,2,2,1,-1,-1,1,-1],[2,2,2,1,-1,1,-1,-1],[2,2,2,1,1,-1,-1,-1]]

h = Solution()
print(h.permuteUnique(input1))
#print({tuple(i) for i in h.permuteUnique(input2)} == {tuple(i) for i in test})

end = time.time()
print(end - start)


        
