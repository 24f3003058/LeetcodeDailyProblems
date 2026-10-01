class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid= {")":"(","}":"{","]":"["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1]!=valid[char]:
                    return False
                stack.pop()
        return len(stack) == 0
