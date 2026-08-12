class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch_map = {"}": '{', ']': '[', ')': '('}
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            elif stack == []:
                return False
            elif stack != [] and stack[-1] != ch_map[ch]:
                return False
            else:
                stack.pop()
        return stack == []