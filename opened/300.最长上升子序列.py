#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.23%)
# Likes:    361
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 89.8K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#

# @lc code=start
'''
第一次尝试的思路如下
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m=[nums[0]]
        ans = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                ans+=1
        
        return ans
'''
WA:[4,10,4,3,8,9]
对应计算的结果是:[1,2,2,2,3,4]。但我们发现，以第二个4结尾的最长上升序列长度是1，序列为[4].
计算以第二个4为结尾的最长上升序列长度时，依据是f(第二个4) = f(10) if 4<10 else f(10)+1.
但正确结果是:以第二个4为结尾的最长上升序列不能依赖于以10为结尾的最长上升序列长度，ATTENTION:f(x)计算的序列结尾必须是num[x]
'''


'''
所以，我们需要针对前一种错误，进行纠正，
我们要做的是，考虑nums[i]的时候，不能只考虑前一个数nums[i-1]，因为f(i)不一定总是能包括nums[i-1],有可能包括nums[i-2]...
第二次尝试如下：
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = [1 for _ in range(len(nums))]
        # ans = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    m[i] = max( m[i], m[j]+1 )
                else:
                    m[i] = m[j]

        return max(m)
'''
本次的错误在于
else:
    m[i] = m[j]
如果nums[i]<=nums[j]
那么，以nums[i]为结尾这个序列是不能由以nums[j]为结尾的序列更新的。当前状态的更新只能来源于在i-1,i-2...中找到了可以上升的序列，使得序列长度+1，或者都没有找到，那么维持现状。
'''

'''
AC
对，'我从哪里来?' 当前状态i来源于 以nums[i-1],nums[i-2],...为结尾的那些序列长度，如果当前i大于之前那些序列的结尾，则当前的结果+1,否则维持现状.
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        m = [1 for _ in range(len(nums))]
        # ans = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    m[i] = max(m[i], m[j]+1)
                # else:
                #     m[i] = m[j]
        # print(m)
        return max(m)
'''
执行用时 :
1568 ms
, 在所有 python3 提交中击败了
8.60%
的用户
内存消耗 :
12.8 MB
, 在所有 python3 提交中击败了
99.54%
的用户
'''
# @lc code=end

