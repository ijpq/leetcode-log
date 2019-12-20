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



'''
结合二分查找的优化
我们任何一个局面，从两个地方来，一个是维持局面，一个是之前的最大长度+1，所以m数组是递增的数组，所以在搜索‘之前的最大长度时，可以用二分查找，将O(n)的搜索优化到O(logn)’.
但如果仍然在m中存储最长序列长度,即使找到合适的m[j],可以使m[i]更新,但nums[j]不一定能够小于nums[i],二分是无意义的
---
所以需要配合二分时,怎么将m存储的内容改一下,
1.使得二分有意义呢,就是说使得二分找到的那个mid就是我们直接能需要的mid?
2.如果更改了m存储的内容,那么之前n方解法的转移方程也需要改?
3.如果m存储的内容不是递增的,那么二分就可以依据m的索引来进行.
---
定义m[i]存储的是长度为i的众多解中,最小的序列末尾长度.
这样的话,
我们可以在当前的局面m[i]下,从后向前考察m[i-1],...,直到一个m[x]的值小于nums[i],此时m[x+1]的值更新为nums[i]啊啊啊不对不会了
'''
def binary_update(target,nums, m,left,right):
    # while left<right:
    #     mid = (left + right) /2 
        
    #     if m[mid] + 1  <= m[target]: # 如果无法得到更新,则继续查找更大的m[x]
    #         binary_update(target=target,nums,m,left=mid+1,right=right)
    #     else:
    #         if nums[mid] < nums[target]:
    #             return 
    #         else:
    #             binary_update(target=target,nums,m,left=0,right=mid-1)
        
    # #最后一个可能更新的m[x]
    # if 
            

        
    pass
import sys
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        m = [sys.maxsize for _ in range(len(nums))]
        m[0]=nums[0]
        for i in range(1, len(nums)):
            for j in range(i):
                pass
            
        return res
# @lc code=end

