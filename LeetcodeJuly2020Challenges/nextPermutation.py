import time

start = time.time()

class Solution:
    def nextPermutation(self,inputs):
        if len(inputs) > 2:
##            return inputs
##        else:
            i = len(inputs) - 2
            j = len(inputs) - 2
            while i > -1:
                if inputs[i] < inputs[-1]:
                    print("found position to change!")
                    while inputs[i] < inputs[j]:
                        j = j - 1
                    inputs[i], inputs[j+1] = inputs[j+1], inputs[i]
                    print(inputs)
                    break
##                    return inputs
                else:
                    inputs.append(inputs.pop(i))
                    print(inputs)
                i = i - 1
                
    
inputs = [1,2,3,2,1]
h = Solution()
print(h.nextPermutation(inputs))

end = time.time()
print(end - start)
        
