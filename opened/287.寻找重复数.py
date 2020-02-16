#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (61.50%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 47.1K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
# 
# 示例 1:
# 
# 输入: [1,3,4,2,2]
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,3,4,2]
# 输出: 3
# 
# 
# 说明：
# 
# 
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
# 
# 
#

# @lc code=start


def partition(nums, left, right):
    i = left-1
    pivot = nums[right]  # 主元,做划分用
    for j in range(left, right):  # j= left to right-1
        if nums[j] <= pivot:  # 如果当前元素小于主元,就使当前元素放到nums[i]处,所有i及i左侧的元素都小于主元
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
    def findDuplicate(self, nums: List[int]) -> int:
        QuickSort(nums, left=0, right=len(nums)-1)
        for s,i in enumerate(nums):
            if i == nums[s+1]:
                return i
        
# @lc code=end

