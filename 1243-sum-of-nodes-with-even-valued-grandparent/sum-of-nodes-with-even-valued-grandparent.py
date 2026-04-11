# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def evenGrandPa(node, parent, grandparent):
            if not node:
                return 0
            res = 0
            if grandparent and grandparent.val % 2 == 0:
                res += node.val
            
            res += evenGrandPa(node.left, node, parent)
            res += evenGrandPa(node.right, node, parent)

            return res
                 
        return evenGrandPa(root, None, None)
        