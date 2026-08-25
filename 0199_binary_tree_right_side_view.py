# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rightview(node,level,ans):
            if not node:
                return
            if level==len(ans):
                ans.append(node.val)
            if node.right:
                rightview(node.right,level+1,ans)
            if node.left:
                rightview(node.left,level+1,ans)
        ans=[]
        rightview(root,0,ans)
        return ans
        