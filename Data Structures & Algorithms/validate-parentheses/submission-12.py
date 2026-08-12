class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch_map = {"}": '{', ']': '[', ')': '('}
        for ch in s:
            if ch in ch_map:
                if stack and stack[-1] == ch_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return stack == []