#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (65.45%)
# Likes:    235
# Dislikes: 0
# Total Accepted:    56K
# Total Submissions: 85.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 0:
#             return []
#         ret = [[1]]
#         for row in range(1,numRows):
#             in_ret = [1]
#             for col in range(1,(row+1)-1):
#                 print('x:{},y:{};x:{},y:{}'.format(row-1,col-1,row-1,col))
#                 ele = ret[row-1][col-1] + ret[row-1][col]
#                 in_ret.append(ele)
#             in_ret.append(1)
#             ret.append(in_ret)
#         return ret
                
# @lc code=end




def generate(numRows):
    #基本情况
    if numRows == 1:
        return [[1]]
    # if numRows == 2:
    #     return [1,1]

    # 递推关系
    upper = generate(numRows-1)#上一层的杨辉三角结果
    cur = [1]
    for i in range(1,numRows-1):
        cur.append(upper[-1:][i-1]+upper[-1:][i])
    cur.append(1)
    upper.append(cur)

    return upper

generate(5)