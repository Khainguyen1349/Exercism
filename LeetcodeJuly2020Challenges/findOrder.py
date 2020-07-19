import time

start = time.time()

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        l = [i for i in range(numCourses)]
        print('List init: ', l)
        for i in prerequisites:
            print('Checking item: ', i)
            if l.index(i[0]) < l.index(i[1]):
                print('Swapping')
                ind1 = l.index(i[1])
                l[l.index(i[0])] = i[1]
                l[ind1] = i[0]
        return l

input1 = 2
input2 = [[0,1]]
h = Solution()
print(h.findOrder(input1, input2))

end = time.time()
print(end - start)
        
