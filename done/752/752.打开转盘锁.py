#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# https://leetcode-cn.com/problems/open-the-lock/description/
#
# algorithms
# Medium (47.58%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 12.3K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 
# 
# 示例 2:
# 
# 
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。
# 
# 
# 示例 3:
# 
# 
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
# 
# 
# 示例 4:
# 
# 
# 输入: deadends = ["0000"], target = "8888"
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 死亡列表 deadends 的长度范围为 [1, 500]。
# 目标数字 target 不会在 deadends 之中。
# 每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。
# 
# 
#


# @lc code=start
from queue import Queue
class Solution:
    def __init__(self):
        print('1')
    def openLock(self, deadends, target: str) -> int:
        if '0000' in deadends:
            return -1
            
        self.start = '0000'
        # self.queue = []
        self.visited = {}
        q= Queue()
        self.deadends = set(deadends)
        self.head, tail = 0,0
        
        step = 0
        q.put(('0000',0))
        # self.queue.append((self.start,step))
        # self.tail = 1 
        
        # while not self.isempty():
        while not q.empty():
            #无解的条件是队空，但队列中没有出现过target
            # 如果target出现在队列中可终止，或队空可终止
            # current, step = self.queue[self.head]#取队头
            current, step = q.get()
            # self.visited[current] = 1#队头标记
            # if current not in self.deadends:
            #     self.deadends.add(current)

            adj_node = self.increment(current)#找可行邻节点
            if target in adj_node:
                # return self.queue[self.head][1] + 1
                return step + 1
            if len(adj_node)!=0:
                step +=1
                # self.enqueue(adj_node,step)#林结点入队
            for node in adj_node:
                q.put((node,step))
                if node not in self.deadends:
                    self.deadends.add(node)
            # print(step)
            # self.dequeue(current)

    
        return -1

    def isempty(self):
        return True if self.head == self.tail else False

    def enqueue(self,node_list,step):
        for node in node_list:
            self.queue.append((node,step))
            self.tail += 1

    def dequeue(self,node):
        self.head += 1

    def increment(self,current:str):
        # 死亡结点和访问过的结点不入队
        # 返回可行的邻节点
        assert isinstance(current,str),'type current error'
        ret = []
        for state in ['+','-']:
            for bit in range(len(current)):
                if state == '+':
                    change_str = current[:bit]+str((int(current[bit])+1)%10)+current[bit+1:]
                    if change_str in self.deadends:
                        continue
                if state == '-':
                    change_str = current[:bit]+str((int(current[bit])-1)%10)+current[bit+1:]
                    if change_str in self.deadends:
                        continue
                ret.append(change_str)
        return ret
        
        
s=Solution()   
r=s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888")
print('r',r)

"""
可以将转盘锁当前的状态视为二维平面图上的一个坐标点，与此点相邻的坐标点有八个，可以理解为相应的增加/减少每一位数字对应的新状态。通过BFS或dfs的方法，如果当前初始状态（或target）经过任何路径都无法达到target（或初始状态）
则返回1，否则返回步长计数器。
不可行
"""
        
# @lc code=end

