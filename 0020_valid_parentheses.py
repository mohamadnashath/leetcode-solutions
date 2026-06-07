class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack:
                    return False
                f = stack.pop()
                if f != pairs[i]:
                    return False
        return not stack
