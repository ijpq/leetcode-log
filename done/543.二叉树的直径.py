#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (47.08%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 40.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
# 
# 示例 :
# 给定二叉树
# 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
# 
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        return max(self.getdepth(root.left)+self.getdepth(root.right), left_diameter, right_diameter)
    
    def getdepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.right is None:
            return self.getdepth(root.left)+1
        if root.left is None:
            return self.getdepth(root.right)+1
        
        return max(self.getdepth(root.left),self.getdepth(root.right))+1
        
# @lc code=end

