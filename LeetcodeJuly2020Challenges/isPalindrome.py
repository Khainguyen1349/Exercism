import time

start = time.time()

class Solution:
    def isPalindrome(self, head) -> bool:
        i = len(head)
        j = 0
        #flag = True
        while i > j:
            if not(head[i-1] == head[j]):
                print(head[i-1],',',head[j])
                return False
            i = i - 1
            j = j + 1
        return True
            
    
inputs = [1,10,3,2,1]
h = Solution()
print(h.isPalindrome(inputs))

end = time.time()
print(end - start)
        
