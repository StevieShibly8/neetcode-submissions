class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        maxL = height[0]
        maxR = height[len(height)-1]
        while l < r:
            if height[l] <= height[r]:
                water += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                water += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1
        return water