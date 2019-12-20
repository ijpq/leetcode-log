
index有点蠢
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['{','[','(']
        right = ['}',']',')']
        for s,ele in enumerate(s):
            #首先空字符去掉
            if ele == ' ':
                continue
                
            #如果是左 记录索引，压栈
            if ele in left:
                idx = left.index(ele)
                stack.append(ele)
            
                
            #如果是右 非空且匹配，出栈
            elif len(stack)>0 and right.index(ele) == left.index(stack[-1]):
                stack = stack[:-1]
            
            #否则失败
            else:
                return False
                
            
        # print('stack',stack)
        if len(stack) != 0:
            return False
        else:
            return True
        
```
