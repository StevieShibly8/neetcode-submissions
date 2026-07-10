class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        length = len(heights)
        l = 0
        r = length-1
        while l != r:
            water = max(water, (r-l)*min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return water