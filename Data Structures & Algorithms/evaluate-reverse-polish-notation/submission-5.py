class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-/*"
        for t in tokens:
            if t in operands:
                num1, num2 = int(stack.pop()), int(stack.pop())
                if t == "+":
                    result = num1 + num2
                elif t == "-":
                    result = num2 - num1
                elif t == "*":
                    result = num1 * num2
                elif t == "/":
                    result = num2 / num1
                stack.append(result)
            else:
                stack.append(t)
        
        return int(stack[-1])
                