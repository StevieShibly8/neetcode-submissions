class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        tempIndex = defaultdict(list)
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if i == 0:
                stack.append(temp)
                tempIndex[temp] = [i]
            else:
                if temp <= stack[-1]:
                    stack.append(temp)
                    tempIndex[temp].append(i)
                else:
                    while stack and stack[-1] < temp:
                        lastTemp = stack.pop()
                        indexLastTemp = tempIndex[lastTemp].pop()
                        ans[indexLastTemp] = i - indexLastTemp
                    stack.append(temp)
                    tempIndex[temp].append(i)

        return ans