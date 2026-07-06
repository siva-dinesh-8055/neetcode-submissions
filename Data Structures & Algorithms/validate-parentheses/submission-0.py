class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        n = len(s) 
        for i in range(n):
            if s[i] in {'(', '{', '['}:
                stack.append(s[i]) 

            elif stack and (stack[-1] == '(' and s[i] == ')'):
                stack.pop() 

            elif stack and (stack[-1] == '[' and s[i] == ']'):
                stack.pop() 

            elif stack and (stack[-1] == '{' and s[i] == '}'):
                stack.pop()

            else:
                return False 

        return len(stack) == 0