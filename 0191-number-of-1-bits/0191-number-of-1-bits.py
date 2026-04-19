class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            # Check if the last bit is 1
            if n % 2 == 1:
                count += 1
            # Move to the next bit (divide by 2)
            n = n // 2
        return count
        