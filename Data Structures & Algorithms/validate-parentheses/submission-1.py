class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opentoclose = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in opentoclose:
                if not stack or (stack[-1]  != opentoclose[c]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack