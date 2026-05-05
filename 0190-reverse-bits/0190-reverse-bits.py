class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # We must process all 32 bits
        for i in range(32):
            # 1. Shift our result to the left to make room for a new bit
            res = res << 1
            
            # 2. Get the last bit of n (using bitwise AND)
            last_bit = n & 1
            
            # 3. Add that bit to our result
            res = res | last_bit
            
            # 4. Shift n to the right to discard the bit we just used
            n = n >> 1
            
        return res