class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxL = [0]*length
        maxR = [0]*length
        currMaxL = 0
        currMaxR = 0
        for i in range(length):
            maxL[i] = currMaxL
            maxR[-i-1] = currMaxR
            currMaxL = max(currMaxL, height[i])
            currMaxR = max(currMaxR, height[-i-1])
        
        return sum([max(0, min(x, y)-z) for x,y,z in zip(maxL, maxR, height)])