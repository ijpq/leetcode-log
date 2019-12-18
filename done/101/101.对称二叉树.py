#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (48.88%)
# Likes:    534
# Dislikes: 0
# Total Accepted:    76.6K
# Total Submissions: 155.7K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def check(que):
    #总是入队一整层后，检查对称性
    i, j = 0, len(que)-1
    while i <= j:
        if que[i][0] is None and que[j][0] is None:
            i += 1
            j -= 1
            continue
        elif que[i][0] is None or que[j][0] is None:
            return False
        elif que[i][0].val == que[j][0].val:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True
    pass


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        que = []
        depth = 0
        counter = 0
        tail = 1
        que.append((root, depth))
        while len(que) > 0:
            cur, depth = que.pop(0)  # 出队

            counter += 1  # 全局节点计数
            if cur is not None:
                que.append((cur.left, depth+1))  # 左右孩子入队
                que.append((cur.right, depth+1))
            if counter == tail:  # 如果出队节点是当前层尾节点
                # FIXME  不一定是完全二叉树,第i层不一定有2**(depth+1)个节点，因为上一层可能有空
                tail += len(que)
                if check(que):
                    continue
                    #此时队列中应是下一层(depth)的所有节点，此时应该对队列进行检查
                else:

                    return False

        return True
# @lc code=end

