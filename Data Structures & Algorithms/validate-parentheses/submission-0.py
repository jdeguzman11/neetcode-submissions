class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ["(", "{", "["]

        for ch in s:
            if ch in valid:
                stack.append(ch)
            
            else:
                if stack:
                    if ch == ")" and stack[-1] == "(":
                        stack.pop(-1)
                    
                    elif ch == "}" and stack[-1] == "{":
                        stack.pop(-1)

                    elif ch == "]" and stack[-1] == "[":
                        stack.pop(-1)
                    
                    else:
                        return False
                
                else:
                    return False
        
        return len(stack) == 0
