# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        if not root:
            return self.res
        q = deque()
        q.append(root)

        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                right = node.val
            self.res.append(right)
        

        return self.res
















        # self.res = []

        # def dfs(root, level):
        #     if not root:
        #         return
            
        #     if level == len(self.res):
        #         self.res.append(root.val)
        #     dfs(root.right, level + 1)
        #     dfs(root.left, level + 1)
        
        # dfs(root, 0)
        # return self.res
        
        
        