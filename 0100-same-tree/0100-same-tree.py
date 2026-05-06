class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. If both nodes are empty, they are the same
        if not p and not q:
            return True
        
        # 2. If one is empty but the other isn't, they are different
        if not p or not q:
            return False
        
        # 3. If the values are different, they are different
        if p.val != q.val:
            return False
        
        # 4. Check if the left and right sides are also the same
        # This keeps going until it hits the bottom of the tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)