# Leetcode

# 1.two sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.//返回索引值

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.//只有唯一解,一个元素不能用两次

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```



## C

```c
/*
- Note: The returned array must be malloced, assume caller calls free().
*/
  int* twoSum(int* nums, int numsSize, int target) {
  static int re[2];
  int i=0;
  for (i=0;i<numsSize;i++)
  {
      int j=numsSize-1;
      while(i<j)
      {
          if ((*(nums+i)+*(nums+j))==target){
              re[0]=i;
              re[1]=j;
              return re;
          }
          else {j--;}
      }
  }
  return re;
  }
```

