# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            
            elif p.val < current.val and q.val < current.val:
                current = current.left
            
            else:
                return current
            

