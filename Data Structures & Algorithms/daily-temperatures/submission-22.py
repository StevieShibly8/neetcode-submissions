class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                lastTempInd = stack.pop()
                ans[lastTempInd] = i - lastTempInd
            stack.append(i)
        return ans