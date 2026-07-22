class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for ch in s:
            if ch in valid_map:
                stack.append(valid_map[ch])
            elif not stack or stack.pop() != ch:
                return False

        return len(stack) == 0