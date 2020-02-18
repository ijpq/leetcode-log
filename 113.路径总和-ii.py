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

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path = []
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            stack = []
            ret=[]
            cur = root
            while True: 
                
                while cur is not None:
                    #visit(cur)
                    
                    if qiuhe(path, cur.val) > sum:
                        break
                    path.append(cur.val)

                    if cur.right is not None:
                        stack.append(cur.right)

                    cur = cur.left
                if len(stack) == 0:
                    break

                cur = stack.pop()
            return ret
                
                
                
            
            
        
# @lc code=end

