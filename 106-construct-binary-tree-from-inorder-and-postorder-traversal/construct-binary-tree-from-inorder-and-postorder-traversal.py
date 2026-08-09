# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
      
        pos = {}
        for i in range(len(inorder)):
            pos[inorder[i]] = i
        #print(pos)
        def build(left, right):
            #print(left, right)
            if left > right:
                return None
                
            rootval = postorder.pop()
            root = TreeNode(rootval)
            mid = pos[rootval]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
        