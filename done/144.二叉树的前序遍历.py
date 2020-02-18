#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (62.41%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    65.9K
# Total Submissions: 103K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''递归'''
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         ret = []
#         if root is None:
#             return None
#         left = self.preorderTraversal(root.left)
        
#         right = self.preorderTraversal(root.right)
#         ret.append(root.val)
#         if left is not None:    
#             ret.extend(left)
#         if right is not None:
#             ret.extend(right)
        
#         return ret

'''自己写的迭代'''
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return root
#         ret = []
#         stack = []
#         stack.append(root)
        
#         while len(stack) != 0:
#             cur = stack.pop()

#             ret.append(cur.val) # eqs visit
#             if cur.right is not None:
#                 stack.append(cur.right)
#             if cur.left is not None:
#                 stack.append(cur.left)
#         return ret

'''标准版本迭代'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret=[]
        cur = root
        while True:
            
            while cur is not None:
                ret.append(cur.val)

                if cur.right is not None:
                    stack.append(cur.right)

                cur = cur.left
            if len(stack) == 0:
                break

            cur = stack.pop()
        return ret

# @lc code=end

