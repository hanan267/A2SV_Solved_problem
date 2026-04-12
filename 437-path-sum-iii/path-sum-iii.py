# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        pref = defaultdict(int)
        pref[0] = 1

        def dfs(node, currSum):

            if not node:
                return 0
            
            currSum += node.val

            count = pref[currSum-targetSum]

            pref[currSum] += 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            pref[currSum] -= 1

            return count
        
        return dfs(root, 0)

