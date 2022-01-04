import time

start = time.time()

class Solution:
    def convert(self, s, numRows):
        L = []
        for i in range(numRows):
            if i == 0:
                L.append("".join([s[i] for i in range(len(s)) if not i%(2*numRows - 2)]))
            if i == (numRows-1):
                L.append("".join([s[i] for i in range(len(s)) if not i%(2*numRows - 2) - (2*numRows -(numRows + 1))]))
            else:
                L.append("".join([s[i] for i in range(len(s)) if not ((i%(2*numRows - 2) - i) and (i%(2*numRows - 2) - (2*numRows - 2 - i)))]))
        return "".join(L)
        #return "".join([s[i] for i in range(len(s)) if not i%(2*numRows - 2) - 0]) \
               #+ "".join([s[i] for i in range(len(s)) if not ((i%(2*numRows - 2) - 1) and (i%(2*numRows - 2) - (2*numRows - 3)))]) \
               #+ "".join([s[i] for i in range(len(s)) if not i%(2*numRows - 2) - (2*numRows -(numRows + 1))])
        #return sout
        #for i in range(numRows):
            #s.join()
        
    
inputs = "PAYPALISHIRING"
input2 = 'abcdefghijklmnopqrstuvwxyz'
h = Solution()
print(h.convert(input2,3))

end = time.time()
print(end - start)
        
