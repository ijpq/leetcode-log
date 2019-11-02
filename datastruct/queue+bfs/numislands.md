# 题目
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

## 思路 1 **超时,O(N^3)**
对每个点进行一次 BFS, BFS 访问到的点给 visited = 1, 每次从一个 unvisited 开始 BFS时, 累加一个岛屿, 跳过所有非岛屿的点.

```python
import pdb
class Solution(object):
    def __init__(self):
        print('init')
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        self.queue = []
        # self.queue = [e for out in grid for e in out]
        # self.queue[:] = 0
        self.count = 0
        self.grid = grid

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.visited[i][j] != 1 and self.grid[i][j] == '1':  # not visted and island
                    # pdb.set_trace()
                    self.count += 1
                    print('count=',self.count)
                    self.queue.append((i, j))
                    print('join {},{}'.format(i,j))
                    self.bfs(i, j)
                # elif self.visited[i][i] == 1 :
                #     continue
                # elif self.
        return self.count

    def bfs(self, i, j):
        while len(self.queue) != 0:
            x, y = self.pop()
            self.visited[x][y] = 1
            self.check(x, y)

        pass

    def pop(self):
        # return current node and forward a index
        x, y = self.queue[0]
        self.queue = self.queue[1:]
        return x, y
        pass

    def check2(self,i,j):
        if i >= 0 and i <= (len(self.grid) - 1 ) and j >= 0 and j <= (len(self.grid[0]) - 1):
            if self.visited[i][j] != 1 and self.grid[i][j] == '1':
                self.queue.append((i, j))
                print('join {},{}'.format(i,j))

    def check(self, i, j):
        self.check2(i-1,j)
        # if i -1 >=0 :
        #     if self.visited[i - 1][j] != 1 and self.grid[i -1 ][j]=='1':
        #         self.queue.append((i -1 , j))
        self.check2(i+1,j)
        # if i+1 <= len(self.grid) -1 :
        #     if self.visited[i + 1][j] != 1 and self.grid[i+1][j]=='1' :
        #         self.queue.append((i+1, j))
        self.check2(i,j-1)
        # if j-1 >= 0 :
        #     if self.visited[i][j - 1] != 1 and self.grid[i][j-1]=='1' :
        #         self.queue.append((i, j-1))
        self.check2(i,j+1)
        # if j+1 <= len(self.grid[0]) -1:
        #     if self.visited[i][j + 1] != 1 and self.grid[i][j+1]=='1' :
        #         self.queue.append((i, j+1))

print('x')
s = Solution()
x = s.numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]])
print(x)

