# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root, arr):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)
            inorder(root.left, arr)
            inorder(root.right, arr)
        
        parr, qarr = [], []
        inorder(p, parr)
        inorder(q, qarr)

        print(parr, qarr)

        if parr == qarr:
            return True
        else:
            return False
        