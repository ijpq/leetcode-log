#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (73.99%)
# Likes:    534
# Dislikes: 0
# Total Accepted:    78.3K
# Total Submissions: 105.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    import copy
    def permute(self, nums):
        
        def helper(path, choice):
            if len(path) == len(nums) and len(choice) == 0:

                '''ATTENTION'''
                cur_path = copy.deepcopy(path)
                ret.append(cur_path)
                del cur_path
                '''ATTENTION'''
                return
            
            for i in range(len(choice)):
                #make choice
                cur_choice = choice[:i]+choice[i+1:]
                path += [choice[i]]
                helper(path=path, choice=cur_choice)
                
                #backtrack
                path.pop()


            
        ret = []
        helper(path=[],choice=nums)
        return ret
# @lc code=end

