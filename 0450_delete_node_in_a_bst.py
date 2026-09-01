# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            return self.delete(root)
        temp=root
        while temp is not None:
            if temp.val>key:
                if temp.left is not None and temp.left.val==key:
                    temp.left=self.delete(temp.left)
                else:
                    temp=temp.left
            else:
                if temp.right is not None and temp.right.val==key:
                    temp.right=self.delete(temp.right)
                else:
                    temp=temp.right
        return root
    def delete(self,node:TreeNode):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            right_tree=node.right
            last_right=self.lastright(node.left)
            last_right.right=right_tree
            return node.left
    def lastright(self,node: TreeNode):
        while node.right is not None:
            node=node.right
        return node