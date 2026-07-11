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
        
        minLR = [min(x, y) for x,y in zip(maxL, maxR)]
        print(maxL)
        print(maxR)
        print(minLR)
        return sum([max(0, x-y) for x,y in zip(minLR, height)])