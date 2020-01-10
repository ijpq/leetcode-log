#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (62.66%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    58.8K
# Total Submissions: 92.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        在当前的局面下,如果无法交换,则返回当前局面的head;如果可以交换,则1交换当前两节点,2交换后面两节点,3建立当前局面和后面局面的连接.
        '''
        if head is None or head.next is None:
            return head
        # swap current node
        new_ = ListNode(0)
        new_.next = head.next
        head.next = head.next.next
        new_.next.next = head
        head = new_.next
        del new_
        # swap next two nodes and return next head (two_head)
        two_head = self.swapPairs(head.next.next)
        # construct link
        head.next.next = two_head
        #return current head
        return head

# @lc code=end

