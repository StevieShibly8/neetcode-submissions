class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ans = []

        for num in tokens:
            if num == "+":  
                ans.append(ans.pop() + ans.pop())
            elif num == "*":
                ans.append(ans.pop() * ans.pop())
            elif num == "-":
                ans.append(-ans.pop() + ans.pop())
            elif num == "/":
                ans.append(int((1/ans.pop())*ans.pop()))
            else:
                ans.append(int(num))

        return ans[0]

