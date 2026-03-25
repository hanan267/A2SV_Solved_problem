class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # stack = []
        
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left

        #     root = stack.pop()
        #     res.append(root.val)
        #     root = root.right
        
        # return res


        

        def helper(node, ans):
            if node:
                helper(node.left, ans)
                res.append(node.val)
                helper(node.right, ans)
        res = []
        helper(root, res)
        return res