class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ans = []

        for num in tokens:
            if num == "+":
                num1 = ans.pop()
                num2 = ans.pop()    
                ans.append(num2 + num1)
            elif num == "*":
                num1 = ans.pop()
                num2 = ans.pop() 
                ans.append(num2 * num1)
            elif num == "-":
                num1 = ans.pop()
                num2 = ans.pop() 
                ans.append(num2 - num1)
            elif num == "/":
                num1 = ans.pop()
                num2 = ans.pop() 
                ans.append(int(num2 / num1))
            else:
                ans.append(int(num))

        return ans[0]

