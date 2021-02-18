import time

start = time.time()

class Solution:
    def maxArea(self, height) -> int:
        le = len(height) -1
        I = sorted(range(le+1), key=lambda k: height[k])
        print('height:',height)
        print('Sorted index:',I)
        w_left = 0
        w_right = 0
        w_max = 0
        last_left = I[le]
        last_right = I[le]
        i = le
        
        if I[le] == le:
            terminate_right = True
            print('Terminate right True')
        else:
            terminate_right = False

        if I[le] == 0:
            terminate_left = True
            print('Terminate left True')
        else:
            terminate_left = False

        while not(terminate_left and terminate_right):
            i = i - 1
            print('--------------------------')
            print('Round:',i,'with value ',height[I[i]],'at position ',I[i])
            if (I[i] > last_right) and (not terminate_right):
                if I[i] == le:
                    terminate_right = True
                    print('Terminate right True')
                w_right = height[I[i]]*(I[i]-last_left)
                print('w_right:', w_right)
                if w_right > w_max:
                    w_max = w_right
                last_right = I[i]
                print('last right:',last_right)
            elif (I[i] < last_left) and (not terminate_left):
                if I[i] == 0:
                    terminate_left = True
                    print('Terminate left True')
                w_left = height[I[i]]*(last_right-I[i])
                print('w_left:', w_left)
                if w_left > w_max:
                    w_max = w_left
                last_left = I[i]
                print('last left:',last_left)

        return w_max




inputs = [1,8,6,2,5,4,8,3,7]
h = Solution()
print(h.maxArea(inputs))

end = time.time()
print(end - start)
        
