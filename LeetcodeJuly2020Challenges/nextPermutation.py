import time

start = time.time()

class Solution:
    def nextPermutation(inputs):
        if len(inputs) < 2:
            return inputs
        else:
            i = len(inputs) - 2
            j = len(inputs) - 1
            while i > -1:
                if inputs[i] < inputs[-1]:
                    print("found position to change!")
                    while inputs[i] < inputs[j]:
                        j = j - 1
                    inputs[i], inputs[j] = inputs[j], inputs[i]
                    print(inputs)
                    return inputs
                else:
                    inputs.append(inputs.pop(i))
                    print(inputs)
                i = i - 1
                
    
inputs = [1,2]
h = Solution()
#print(h.nextPermutation(inputs))
h.nextPermutation('a')

end = time.time()
print(end - start)
        
