class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for ch in s:
            if ch in valid:
                stack.append(valid[ch])
            elif not stack or ch != stack.pop():
                return False
        return len(stack) == 0