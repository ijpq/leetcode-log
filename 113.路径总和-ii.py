#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (58.65%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    29.6K
# Total Submissions: 50.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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

'''先序遍历, 回溯'''
#这里回溯的概念是因为:例如当前面临节点11,要先调用helper(左),此时面临节点7,此轮的左右孩子均为空节点,无返回.再回到面临节点11的轮,接下来调用helper(右)
#面临节点2,找到答案,return.

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        
        def helper(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
                return
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)

        res = []
        helper(root, [], sum_)
        return res




        
                    
                
                
                
            
            
        
# @lc code=end

