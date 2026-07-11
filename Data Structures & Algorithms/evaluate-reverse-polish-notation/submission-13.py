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
                num1, num2 = ans.pop(), ans.pop()  
                ans.append(int(num2 / num1))
            else:
                ans.append(int(num))

        return ans[0]

