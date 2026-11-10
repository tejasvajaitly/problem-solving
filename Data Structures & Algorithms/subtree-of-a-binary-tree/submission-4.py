# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return compare(p.left, q.left) and compare(p.right, q.right)
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if compare(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))




        # self.res = False
        # def compare(p, q):
        #     if not p and not q:
        #         return True
        #     if not p or not q:
        #         return False
        #     if p.val != q.val:
        #         return False
            
        #     return compare(p.left, q.left) and compare(p.right, q.right)
        
        # def dfs(root):
        #     if not root:
        #         return
        #     if root.val == subRoot.val:
        #         val = compare(root, subRoot)
        #         if val == True:
        #             self.res = True
            
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        # return self.res

        