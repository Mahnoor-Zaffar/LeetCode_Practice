# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it's technically symmetric
        if not root:
            return True
        
        # We need a helper to compare two different parts of the tree
        def isMirror(left_side, right_side):
            # 1. If both are empty, they match
            if not left_side and not right_side:
                return True
            
            # 2. If only one is empty, they don't match
            if not left_side or not right_side:
                return False
            
            # 3. Check three things:
            # - Are the values the same?
            # - Does the left's left match the right's right? (The outer edges)
            # - Does the left's right match the right's left? (The inner edges)
            return (left_side.val == right_side.val and 
                    isMirror(left_side.left, right_side.right) and 
                    isMirror(left_side.right, right_side.left))
        
        # Start the comparison with the two children of the root
        return isMirror(root.left, root.right)