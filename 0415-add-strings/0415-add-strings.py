class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        
        # Pointers for the end of both strings
        i = len(num1) - 1
        j = len(num2) - 1
        
        # Loop until both strings are done and there is no carry left
        while i >= 0 or j >= 0 or carry:
            # Convert single characters to numbers using ord()
            # ord('0') is 48, so ord('5') - ord('0') = 5
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Calculate sum and carry
            total = digit1 + digit2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            # Move pointers to the left
            i -= 1
            j -= 1
            
        # The list is currently backwards, so reverse it and join to string
        return "".join(res[::-1])