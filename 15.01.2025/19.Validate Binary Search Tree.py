class Solution:
    def isValidBST(self, root):
        def help(left, node, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            return help(left, node.left, node.val) and help(node.val, node.right, right)
        return help(float('-inf'), root, float('inf'))
