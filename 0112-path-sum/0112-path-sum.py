# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1. If the node is empty, there is no path
        if not root:
            return False
        
        # 2. Subtract the current node's value from the remaining sum
        targetSum -= root.val
        
        # 3. Check if we are at a leaf node (no children)
        if not root.left and not root.right:
            # If we are at a leaf, check if the remaining sum is 0
            return targetSum == 0
        
        # 4. Recursively check the left and right children
        # If either side returns True, then a path exists
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)