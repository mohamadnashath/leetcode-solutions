# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]
        self.small(root,result)
        return result[k-1]
    def small(self,node,result):
        if node is None:
            return
        self.small(node.left,result)
        result.append(node.val)
        self.small(node.right,result)
        