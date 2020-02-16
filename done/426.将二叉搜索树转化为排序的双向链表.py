"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        def helper(root):

            
            if root.left is None and root.right is None:
                return root, root

            if root.left is None:
                head, tail = helper(root.right)
                root.right = head
                head.left = root
                return root, tail

            if root.right is None:
                head, tail = helper(root.left)
                tail.right = root
                root.left = tail
                return head, root
            
            head_left, tail_left = helper(root.left)
            head_right, tail_right = helper(root.right)

            tail_left.right = root
            root.left = tail_left

            root.right = head_right
            head_right.left = root

            return head_left, tail_right

        all_head, all_tail = helper(root)
        all_tail.right = all_head
        all_head.left = all_tail
        head = all_head
        return head

         