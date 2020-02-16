#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#
# https://leetcode-cn.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (35.09%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 12.7K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary
# tree）结构相同，但一些节点为空。
# 
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
# 
# 示例 1:
# 
# 
# 输入: 
# 
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
# 
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
# 
# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
# 
# 
# 示例 3:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
# 
# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
# 
# 
# 示例 4:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
# 
# 
# 注意: 答案在32位有符号整数的表示范围内。
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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """利用层次遍历 & 编号位置 (即宽度优先搜索)
        
        Arguments:
            root {TreeNode} -- [description]
        
        Returns:
            int -- [description]
        """        
        if root is None:
            return 0
        stack = []
        dis = 0
        stack.append([root, 0, 1])# node, depth, position
        cur_depth = -1

        while len(stack) != 0:
            level_length = len(stack)

            # 为了获得最左侧非None节点的pos
            # for i in range(level_length):
            #     cur,_,pos = stack[i]
            #     if cur is not None:
            #         start_pos = pos
            #         break

            for i in range(level_length):
                cur, depth, pos = stack.pop(0)
                if cur is not None:
                    
                    #替代方案, 即非空节点条件下,第一次更新depth时为目标节点
                    if cur_depth != depth:
                        cur_depth = depth
                        start_pos = pos

                    dis = max(dis, pos-start_pos +1)
                    stack.append([cur.left, depth+1, 2*pos])
                    stack.append([cur.right, depth+1, 2*pos+1])

        return dis
                
            
            
            
    
            
# @lc code=end

