#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.22%)
# Likes:    651
# Dislikes: 0
# Total Accepted:    104.9K
# Total Submissions: 203.1K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start
import sys
'''
方法一，牛顿莱布尼茨公式
F(x)表示第x天的股价，那么问题转化为max(F(b)-F(a))
进一步转化为f(x)在a到b上的积分，f(x)应是F()的导函数，那么股价函数的导函数应该是[F(x+1)-F(x)]/[x+1-x],即相邻两天股价的差
所以我们可以一遍计算出差值数组，一遍计算结果
假设股价数据为第0天,...,第n-1天，共n天。
diff[i]表示第i+1天和第i天的股价差,i从0到n-2
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass

'''
方法二
这个思路是最基础的，我们考察第i天卖出股票能获得的最大收益，只需要关注前i-1天中最小值即可。
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = sys.maxsize
        max_val = 0
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            max_profit = prices[i] - min_val
            if max_profit > max_val:
                max_val = max_profit
        return max_val


                
            

# @lc code=end

