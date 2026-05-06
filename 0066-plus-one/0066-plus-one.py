class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, just add 1 and we are done
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and we carry the 1 to the next left digit
            digits[i] = 0
            
        # If the loop finishes, it means we had all 9s (like 999)
        # We need to add a 1 at the very beginning (to get 1000)
        return [1] + digits