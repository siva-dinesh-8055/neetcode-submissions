class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps) 
        res = [0 for i in range(n)] 
        stack = [] 

        for i in range(n - 1, -1, -1):
            while stack and temps[stack[-1]] <= temps[i]: 
                stack.pop() 

            if stack:
                res[i] = stack[-1] - i

            stack.append(i) 

        return res