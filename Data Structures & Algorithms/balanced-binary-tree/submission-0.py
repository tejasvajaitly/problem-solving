# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            self.res = max(self.res, abs(l - r))

            return 1 + max(l, r)

        dfs(root)
        
        if self.res > 1:
            return False
        else:
            return True

        
        