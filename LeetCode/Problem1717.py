class Result:
    def __init__(self, gain, remaining):
        self.gain = gain
        self.remaining = remaining

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x > y:
            r1 = self.removePair(s, 'a', 'b', x)
            r2 = self.removePair(r1.remaining, 'b', 'a', y)
            ans = r1.gain + r2.gain
        else:
            r1 = self.removePair(s, 'b', 'a', y)
            r2 = self.removePair(r1.remaining, 'a', 'b', x)
            ans = r1.gain + r2.gain
        return ans

    def removePair(self, s: str, first: str, second: str, value: int) -> Result:
        stack = []
        gain = 0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                gain += value
            else:
                stack.append(ch)
        return Result(gain, ''.join(stack))
