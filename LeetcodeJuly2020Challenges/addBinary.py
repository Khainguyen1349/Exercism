import time

start = time.time()

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = int(a,2) + int(b,2)
        return '{0:b}'.format(s)
    
input1 = '10101110'
input2 = '11001010'
h = Solution()
print(h.addBinary(input1, input2))

end = time.time()
print(end - start)
        
