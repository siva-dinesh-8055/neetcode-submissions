class Solution:
    def nextSmallElementInd(self, arr):
        n = len(arr)
        res = [n for i in range(n)] 
        stack = [] 
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop() 

            if stack and arr[stack[-1]] < arr[i]:
                res[i] = stack[-1] 

            stack.append(i) 
        return res 

    def preSmallElementInd(self, arr):
        n = len(arr)
        res = [-1 for i in range(n)] 
        stack = [] 
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop() 

            if stack and arr[stack[-1]] < arr[i]:
                res[i] = stack[-1] 

            stack.append(i) 
        return res 

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        PSE = self.preSmallElementInd(heights) 
        NSE = self.nextSmallElementInd(heights)
        print(PSE) 
        print(NSE) 

        largest = 0 

        for i in range(n):
            cal = ((NSE[i] - 1) - (PSE[i] + 1) + 1) * heights[i] 
            largest = max(largest, cal) 

        return largest 