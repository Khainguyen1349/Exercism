import time

start = time.time()

class Solution:
    def maxArea(self, height) -> int:
        le = len(height) -1
        print('height:',height)
        last_left = 0
        last_right = le
        left = 0
        right = le
        min_left = height[left] < height[right]
        w_max = min(height[left],height[right])*(right-left)
        
        while left != right:
            print('--------------------------')
            if min_left:
                left = left + 1
                print('current left:',left)
                if height[left] > height[last_left]:
                    w_max = max(min(height[left],height[right])*(right-left),w_max)
                    min_left = height[left] < height[right]
                    last_left = left
                print('last left:',last_left)
            else:
                right = right - 1
                print('current right:',right)
                if height[right] > height[last_right]:
                    w_max = max(min(height[left],height[right])*(right-left),w_max)
                    min_left = height[left] < height[right]
                    last_right = right
                print('last right:',last_right)

        return w_max




inputs = [1,8,6,2,5,4,8,3,7]
h = Solution()
print(h.maxArea(inputs))

end = time.time()
print(end - start)
        
