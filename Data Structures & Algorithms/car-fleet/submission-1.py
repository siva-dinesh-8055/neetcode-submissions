class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        n = len(pos)
        pair = [(p, s) for p, s in zip(pos, speed)]
        pair.sort(reverse=True)
        """
        we are sorting this in reverse beacuse which one is near 
        to destination the the other ones wont overtake the near one 
        as mentioned in the statement...
        """
        stack = []
        for i in range(n):
            cal = (target - pair[i][0]) / pair[i][1]
            stack.append(cal) 
            '''
            Here we are inserting in to stack and comparing the new appended 
            one's time is less than or equal to already available one 
            because which ever the new ones speed is fully dependent on 
            the alrady naer desytination car's speed ony...
            and using "if" insted of 'while' beacuse we need to compare 
            each emtry with already near one to destination.. 
            '''
            if len(stack) >= 2 and stack [-1] <= stack[-2]:
                stack.pop() 

        return len(stack)