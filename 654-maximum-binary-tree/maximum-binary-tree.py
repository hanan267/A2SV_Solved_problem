# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(array):
            if not array:
                return 
            
            maxval = max(array)
            idx = array.index(maxval)
            root = TreeNode(maxval)
            root.left = dfs(array[:idx])
            root.right = dfs(array[idx+1:])
            return root
        return dfs(nums)