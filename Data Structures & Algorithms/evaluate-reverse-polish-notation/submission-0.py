class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        n = len(tokens) 

        for i in range(n):
            if tokens[i] in {"+", "-", "*", "/"}:
                las = stack.pop() if stack else o
                slas = stack.pop() if stack else 0 

                if tokens[i] == '+':
                    stack.append(slas + las) 

                elif tokens[i] == '-':
                    stack.append(slas - las) 

                elif tokens[i] == '*':
                    stack.append(slas * las) 

                else:
                    stack.append(int(slas / las)) 

            else:
                stack.append(int(tokens[i])) 

        return stack[0]