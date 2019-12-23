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
@冒泡排序:执行i=len(nums)次,每次从头,将相邻比较的胜者继续向后比较,每次使得一个胜者到达最终的位置.因此循环长度可逐步缩减1
此题即使优化冒泡排序也TLE
'''

# class Solution:
#     def check(self, nums, p, q):
#         if nums[p] > nums[q]:
#             temp = nums[p]
#             nums[p] = nums[q]
#             nums[q] = temp
#         return nums
#     def sortArray(self, nums: List[int]) -> List[int]:
#         step=0
#         for i in range(len(nums)):
#             for j in range(len(nums)-1-step):
#                 nums = self.check(nums,j,j+1)
#             step+=1
#         return nums

'''
@快速排序
'''
def partition(nums, left, right):
    i = left-1
    pivot = nums[right]#主元,做划分用
    for j in range(left, right):#j= left to right-1
        if nums[j] <= pivot:#如果当前元素小于主元,就使当前元素放到nums[i]处,所有i及i左侧的元素都小于主元
            i += 1
            #swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        #当前元素大于等于主元时,就直接处理下一个元素.
    #i+1位置是大于等于主元的,和主元换一下仍满足状态条件
    temp = nums[i+1]
    nums[i+1] = nums[right]
    nums[right] = temp
    #最后i及i左侧都是小于主元的,i+1是主元,i+1右侧是大于(等于)主元的
    return i+1


def QuickSort(nums, left, right):
    if left < right:
        p = partition(nums, left, right)
        QuickSort(nums, left=left, right=p-1)
        QuickSort(nums, left=p+1, right=right)

class Solution:

    def sortArray(self, nums) :
        QuickSort(nums, 0,len(nums)-1)
        return nums
        
# @lc code=end
