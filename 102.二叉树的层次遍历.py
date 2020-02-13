#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.69%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    76.5K
# Total Submissions: 125.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        stack = []
        stack.append(root)
        cur_depth = []
        final_node = True
        ret = []
        cur_line = 1
        next_line = 0
        
        while len(stack) != 0 :
            cur = stack.pop(0)
            cur_depth.append(cur.val)

            if cur.left is not None:
                next_line+=1
                stack.append(cur.left)
            if cur.right is not None:
                next_line+=1
                stack.append(cur.right) 


            if len(cur_depth) == 1 and len(cur_depth) == cur_line:#start&final
                cur_line = next_line#更新curline的节点数为下一行的节点数
                next_line = 0
                # 当前行的结果保存
                ret.append(cur_depth)
                cur_depth = []
            
            elif len(cur_depth) == cur_line:#only final
                cur_line = next_line
                next_line = 0
                ret.append(cur_depth)
                cur_depth = []
            
        return ret

            
# @lc code=end

