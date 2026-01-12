def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def h(node):
            if not node:
                return 0
            l=h(node.left)
            r=h(node.right)
            if l == -1 or r == -1:
                return -1
            if abs(l - r) > 1:
                return -1

            return max(l,r)+1
        return h(root)!=-1
