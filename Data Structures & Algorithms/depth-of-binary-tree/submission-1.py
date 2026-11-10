# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
















        # res = float('-inf')

        # def dfs(node, depth):
        #     nonlocal res  # refer to the outer 'res' variable
        #     if not node:
        #         res = max(res, depth)
        #         return
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        
        # dfs(root, 0)

        # return res
            

        