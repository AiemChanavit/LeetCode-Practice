class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left

        return root

solution_instance = Solution()
root = [4,2,7,1,3,6,9]
result = solution_instance.invertTree(root)
print(result)