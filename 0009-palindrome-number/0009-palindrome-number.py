class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_str=str(x)
        rev_str=new_str[::-1]
        return new_str==rev_str
        