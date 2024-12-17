# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if not stack:
                    return False
                if stack.pop() != "(":
                    return False
            elif char == "]":
                if not stack:
                    return False
                if stack.pop() != "[":
                    return False
            elif char == "}":
                if not stack:
                    return False
                if stack.pop() != "{":
                    return False
        if stack:
            return False
        return True