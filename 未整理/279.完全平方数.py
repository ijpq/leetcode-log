
#%% [markdown]
# [TOC]
#%% [markdown]
# 分类:动态规划
#思路1 从暴力算法开始


import sys
def solve1(n):
    ans = get_shortest(n)

def get_shortest(n):
    if n <= 1:#实际不会遇到求0的最短序列，该情况已被包含在i**2==n中;而1的最短序列不能在range中求解，所以单独写在前面;
        return 1
    res = sys.maxsize
    for i in range(1,n):#从1开始，逐步计算剩余值(n-i**2)，并求剩余值的最短序列长度
        if i**2 == n:#如果当前待求解的值已是一个平方数，则最短序列为自身，长度=1;
            return 1
        if i**2 >n:#剩余值一定是正数
            break
        rem = n - i**2
        ans = get_shortest(rem) + 1 # get_shortest()返回第一个子树的根节点的最短序列长度; +1 是序列中加入当前子树根节点与get_shortest()之间边的数字
        if ans < res:#记录当前子树根节点的最短序列长度
            res = ans
    return res
st=time.time()    
n=1000
ans = get_shortest(n)
print('solve {}, ans {}'.format(n,ans))
print('consume:{}'.format(time.time()-st))



#%% [markdown]
# 分类:动态规划
#思路1 加入备忘录机制


import sys
import time
memo=dict()
def solve1(n):
    ans = get_shortest(n)

def get_shortest(n):
    global memo
    ans = memo.get(n,-1)
    if ans!=-1:
        return ans
    else:
        res = sys.maxsize
        for i in range(1,n):#从1开始，逐步计算剩余值(n-i**2)，并求剩余值的最短序列长度
            if i**2 == n:#如果当前待求解的值已是一个平方数，则最短序列为自身，长度=1;
                memo[n] = 1
                return memo[n]
            if i**2 >n:#剩余值一定是正数
                break
            rem = n - i**2
            ans = get_shortest(rem) + 1 # get_shortest()返回第一个子树的根节点的最短序列长度; +1 是序列中加入当前子树根节点与get_shortest()之间边的数字
            if ans < res:#记录当前子树根节点的最短序列长度
                res = ans
        memo[n]=res
        return memo[n]
st=time.time()
n=1000
solve1(n)
print('solve {}, ans {}'.format(n,memo[n]))
print('consume:{}'.format(time.time()-st))



                
        
        
# @lc code=end



# %%
