#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (51.52%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 23K
# Testcase Example:  '[5,2,3,1]'
#
# 给定一个整数数组 nums，将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：[5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
# 
# 
#

# @lc code=start
'''
目标:使用冒泡排序,快速排序,堆排序,插入排序,归并排序.
'''
'''
@冒泡排序
'''
class Solution:
    def check(self, nums, p, q):
        if nums[p] > nums[q]:
            temp = nums[p]
            nums[p] = nums[q]
            nums[q] = temp
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                nums = self.check(nums,j,j+1)
        return nums

        
# @lc code=end

