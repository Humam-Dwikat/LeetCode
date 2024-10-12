# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            current_max_path = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_max_path)

            return node.val + max(left_gain, right_gain)

        if root:
            max_gain(root)

        # The result is stored in self.max_sum
        return self.max_sum
