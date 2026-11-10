class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in open:
                stack.append(c)
            elif (c in close and len(stack) > 0 and stack[len(stack)- 1] == map[c]):
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        