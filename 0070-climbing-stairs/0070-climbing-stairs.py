class Solution:
    def climbStairs(self, n: int) -> int:
        # If there is only 1 step, there is only 1 way (1)
        # If there are 2 steps, there are 2 ways (1+1 or 2)
        if n <= 2:
            return n
        
        # We start with the known ways for the 1st and 2nd step
        first = 1
        second = 2
        
        # For every step from 3 to n, the number of ways to reach it 
        # is the sum of the ways to reach the previous two steps.
        for i in range(3, n + 1):
            current = first + second
            # Update pointers for the next step
            first = second
            second = current
            
        return second    