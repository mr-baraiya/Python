class Solution:
    def isValid(self, s: str) -> bool:
        stack = [' '] * len(s)
        top = -1
        for ch in s:
            if ch == '(':
                top += 1
                stack[top] = ')'
            elif ch == '{':
                top += 1
                stack[top] = '}'
            elif ch == '[':
                top += 1
                stack[top] = ']'
            else:
                if top == -1 or ch != stack[top]:
                    return False
                top -= 1
        return top == -1
