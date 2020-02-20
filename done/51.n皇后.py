#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (68.09%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    26.3K
# Total Submissions: 38.7K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
#

# @lc code=start
class Solution:
    import copy
    def solveNQueens(self, n):
        numQ = 0
        ret = []
        occupation = []

        def helper(row, numQ):
            print('start helper : n = {}, numQ = {}, row = {}'.format(n, numQ, row))
            '''尝试在row,col放置第numQ个Queen'''
            if numQ == n:
                ans = copy.deepcopy(occupation) 
                ret.append(ans)
                print(ret)
                del ans
                return 

            '''important:何时递增row?'''
            # 在第row行,分别对col in range 进行尝试
            for col in range(n):
                print('try at {},{}'.format(row,col))
                if not isvalid(row,col):
                    print('not valid at {},{},beacuse occupation {}'.format(row,col,occupation))
                    continue
                occupation.append([row,col])
                numQ+=1
                print('valid at {},{}, occupation {}, numQ {}'.format(row,col,occupation,numQ))
                # 第row行已不可能,从row+1行开始尝试
                
                print('now occupation = {}, go into helper row={}'.format(occupation, row+1))
                helper(row+1, numQ)
                
                occupation.pop()
                numQ-=1
                print('backtrace, now row={}, numQ={}'.format('row,numQ'))
                
        def isvalid(row,col):
            for x, y in occupation:
                if x == row or y == col:
                    return False
                if x+y == row+col:
                    return False

                if x-y == row-col:
                    return False
            return True
                

        helper(0, 0)
        ans = []
        for solution in ret:
            
            res = []
            for x,y in solution:
                string = '.'*n
                string = string[:y] + 'Q' + string[y+1:]
                string = str(string)
                res.append(string)
            ans.append(res)
        return ans
                
# @lc code=end


