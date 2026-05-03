class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are different first
        if len(s) != len(goal):
            return False
            
        # If we double s, it contains every possible rotation
        # Example: "abcde" + "abcde" = "abcdeabcde"
        # "cdeab" is inside "abcdeabcde"
        return goal in (s + s)