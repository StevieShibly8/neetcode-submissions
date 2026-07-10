class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        length = len(heights)
        for i in range(length-1):
            for j in range(i+1, length):
                water = max(water, (j-i)*min(heights[i], heights[j]))
        return water
