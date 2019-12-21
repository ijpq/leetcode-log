#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (38.99%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    26.2K
# Total Submissions: 65.3K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
#

# @lc code=start
'''
当前的局面:f[i][1]表示第i天偷了获得的最好收益,f[i][0]表示第i天没偷获得的最好收益,目标是求max(f[n-1][0],f[n-1][1])
从哪里来:第i天偷了,那么第i-1天一定不能偷,所以就是i-1天没偷的状态再加上第i天偷了的当天收益,f[i][1]=f[i-1][0]+nums[i]
第i天没偷,那么第i-1天可偷可不偷,f[i][0]=max(f[i-1][0],f[i-1][1])
基本情况:由于转移方程最多存在i-1,所以基本情况应该涵盖i=0
f[0][0]=0;f[0][1]就是第0天偷了,那自然就等于第0天的收益nums[0]
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        f = [[0 for _ in range(2)] for _ in range(len(nums))]
        f[0][0]=0
        f[0][1]=nums[0]
        for i in range(1,len(nums)):
            f[i][0]=max(f[i-1][0], f[i-1][1])
            # f[i][1]=max(f[i-2][0],f[i-2][1]+nums[i-2])
            f[i][1]=f[i-1][0]+nums[i]
        # print(f)
        return max(f[-1][0],f[-1][1])
            
# @lc code=end

