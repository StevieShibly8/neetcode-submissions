class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketRelation = { "(":")",
                            "{":"}",
                            "[":"]" }
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            if bracket in ")}]":
                if stack == []:
                    return False
                if bracketRelation[stack.pop()] != bracket:
                    return False
        if stack == []:
            return True
        return False