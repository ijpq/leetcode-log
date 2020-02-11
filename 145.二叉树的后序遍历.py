#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (70.03%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    49.2K
# Total Submissions: 70.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ret = []
        stack = []
        
        def gotoHLVFL(stack):# 将当前子树的hlvfl节点放到栈顶,并沿途保存节点到栈
            while True:
                top = stack[-1]
                while top.left is not None:# 尽量往左
                    if top.right is not None:# 先让右孩子入栈
                        stack.append(top.right)
                    stack.append(top.left)
                    top = top.left
                
                if top.right is not None:
                    stack.append(top.right)
                    continue
                
                return 0
                
        
        stack.append(root)
        cur = root
        while True:
            if len(stack)==0:
                break
            if stack[-1].left != cur and stack[-1].right != cur:#若栈顶节点不是当前节点的父节点,则必是当前节点的右兄弟节点.如果栈顶是当前节点的右兄弟节点,则根据栈顶节点,找vlhfl
                gotoHLVFL(stack)

            #如果栈顶节点是当前节点的父节点,或是当前节点右兄弟节点子树的vlhfl节点,则从栈顶开始
            cur = stack.pop()
            ret.append(cur.val)
            
        return ret
            
            
                 
            

            
# @lc code=end

