---
layout: post
title: What I learned today (Day 02)
---

## Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

```python
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
```

## Solution 
1. I attempted this problem as DP and created a grid with target size (getting slice of len source) same as source size but turns out we are looking for min not max subsequences.
2. Greedy Solution: found it on leetcode solution using two pointer. time O(M*N).
```python 
# First loop for target 
# second loop for source but it will be inside target but to keep track whether we found a subseq use a flag. if these flag is false after iterating over source then there is no subseq possible so return -1.

target_idx = 0 
subseq_count = 0

while target_idx < len(target): 
    subseq_found = False
    source_idx = 0
    
    while source_idx < len(source) and target_idx < len(target): 
                        # and target since we are incrementing target as well.
        if source[source_idx] == target[target_idx]:
            source_idx += 1
            target_idx += 1
            subseq_found = True
        else:
            source_idx += 1

    if subseq_found == False:
        return -1
    
    subseq_count += 1

return subseq_count 
```

