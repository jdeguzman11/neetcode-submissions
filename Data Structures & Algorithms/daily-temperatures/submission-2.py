class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, prev_temp = stack.pop()
                days = i - prev_i
                result[prev_i] = days
            stack.append((i, temp))
        return result