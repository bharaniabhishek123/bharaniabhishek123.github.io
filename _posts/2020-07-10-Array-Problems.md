---
layout: post
title: What I learned today (Day 15)
---

Consolidating all array problems I have completed as of today.
## Two Sum Problem
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

```python
Given 
nums = [2, 7, 11, 15]
target = 9

nums[0] + nums[1] = 2 + 7 = 9 return [0, 1]
```

## Solution 
1. Brute-Force : Have two loops and iterate over each combination. time-complexity $O(N^2)$ and space complexity
$O(1)$.

2. Create Hash table to reduce lookup time to O(1). While iterating over array, do a loopup for second (complement) was previously visited if yes then that's the answer. time-complexity $O(N)$ and space complexity
$O(N)$.

```python
def twosum(nums:List[int], target:int):
    seen_dict = dict()
    n = len(nums)
    for i in range(n):  
        first = nums[i]
        second = target-first 
        if second in seen_dict:
            return [i, seen_dict.get(second)]
    
    seen_dict[first] = i

    return [] # if no two elements found
```

## 3Sum Problem
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Failed Attempt 
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    
    if n < 3 :
        return []
    
    res = []
    
    unique_indexes = []
    
    for i in range(n):
        target = -nums[i]
        other_two_index = self.twosum(nums, target, i)
        
        if len(other_two_index) ==2 :
            
            other_two_index.append(i)
            if list(sorted(other_two_index)) not in unique_indexes:
                unique_indexes.append(list(sorted(other_two_index)))
    
    for record in unique_indexes:
        
        arr = sorted([nums[record[0]],nums[record[1]], nums[record[2]]])
        if sum(arr) ==0 and arr not in res:
            res.append(arr)
    
    return res
```
