class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Clean the string
        # Keep only letters and numbers, and make them lowercase
        cleaned_chars = []
        for char in s:
            if char.isalnum():
                cleaned_chars.append(char.lower())
        
        # Step 2: Check if it reads the same forward and backward
        # We can compare the list with its reverse
        return cleaned_chars == cleaned_chars[::-1]    