# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        n = len(preorder)-1
        postIdx = {}

        for idx, val in enumerate(postorder): # val ->> idx
            postIdx[val] = idx

        def buildRoot(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None
            
            root = TreeNode(preorder[i1])

            if i1 != i2 and j1 != j2:

                leftRoot = preorder[i1+1]
                mid = postIdx[leftRoot]
                leftSize = mid - j1 + 1

                root.left = buildRoot(i1+1, i1+leftSize, j1, mid)
                root.right = buildRoot(i1+leftSize+1, i2, mid+1, j2-1)

            return root

        return buildRoot(0, n, 0, n)

















