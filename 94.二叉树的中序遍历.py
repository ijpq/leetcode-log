#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (70.01%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 144K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        
        if root is None:
            return root

        cur = root


        while True:
        
            while cur is not None:#push L0,L1,...,Ld
                stack.append(cur)
                cur = cur.left

            if len(stack) == 0: # current node is empty and no father node
                break

            cur = stack.pop()

            ret.append(cur.val) # visit current node

            cur=cur.right # eqs dengjunhui datastruct code 5.15, inorder(Ti)



        return ret
            

#TODO 空间复杂度O1的中序迭代算法
                
            
            
            
            
        
# @lc code=end

