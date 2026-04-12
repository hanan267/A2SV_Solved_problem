# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

         
        def dfs(node, arr, Sum):
            if not node:
                return
            
            arr.append(node.val)
            Sum += node.val

            if not node.left and not node.right and Sum == targetSum:
                res.append(arr.copy())
            
            dfs(node.left, arr, Sum)
            dfs(node.right, arr, Sum)

            arr.pop()

        res = []

        dfs(root, [], 0)
        return res





























        # def dfs(node, arr, currSum):

        #     if not node:
        #         return 

        #     currSum += node.val
        #     arr.append(node.val)

        #     if not node.left and not node.right:
        #         if currSum == targetSum:
        #            res.append(arr.copy())

        #     dfs(node.left,arr, currSum)
        #     dfs(node.right,arr, currSum)

        #     arr.pop()
        
        
        # res = []
        # arr = []
     
        # dfs(root, arr, 0)
        # return res

            