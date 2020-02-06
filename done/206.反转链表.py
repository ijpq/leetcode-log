#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (66.67%)
# Likes:    755
# Dislikes: 0
# Total Accepted:    151.3K
# Total Submissions: 226.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        if head.next == None:# basic condition
            return head
            pass

        ret = self.reverseList(head.next)# 记录整个链表的头结点

        head.next.next = head # 让后一个节点指向当前节点
        head.next = None # 这句的目的是逆转完整个链表后,tail.next要指向none,避免tail和倒数第二个node循环连接


        return ret
# @lc code=end

