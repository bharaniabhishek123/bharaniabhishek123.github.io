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

## Important Learning  - Iterative Python program to check if a string is subsequence of another string 
```python

# Returns true if str1 is a subsequence of str2 
def isSubSequence(str1,str2): 
    """ returns True if str1 is subsequence of str2
        example
        'ace' is subsequence of 'abcde'
        'bb' is not subsequence of 'abcde'
    """  
    m = len(str1) 
    n = len(str2) 
      
    j = 0    # Index of str1 
    i = 0    # Index of str2 
      
    # Traverse both str1 and str2 
    # Compare current character of str2 with  
    # first unmatched character of str1 
    # If matched, then move ahead in str1 
      
    while j<m and i<n: 
        if str1[j] == str2[i]:     
            j = j+1    
        i = i + 1
          
    # If all characters of str1 matched, then j is equal to m 
    return j==m 
```      

## Number of Matching Subsequences
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

```python
Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
```

## Solution 
1. getting timeout on the below solution 

```python
def subseq1(self, word1, word2):
    """ returns True if word1 is subsequence of word2
        example
        ace is subsequence of abcde
        bb is not subsequence of abcde            
    """        
    # word1 = bb
    # word2 = abcde
    word1_idx = 0
    word2_idx = 0

    while word1_idx < len(word1) and word2_idx < len(word2):

        if word2[word2_idx] == word1[word1_idx]:
            word1_idx +=1
        word2_idx +=1 
    
    return word1_idx == len(word1)    

def subseq2(self, word1, word2):
    c2 = Counter(word2)
    c1 = Counter(word1)
    
    for c1_ch, c1_count in c1.items():
        if c1_ch not in c2 or c1_count > c2.get(c1_ch) :
            return False
    return True
    

def numMatchingSubseq(self, S: str, words: List[str]) -> int:
    count_subseq = 0
    
    for word in words:
        if self.subseq1(word, S): # or self.subseq2(word,S)
            count_subseq += 1
    
    return count_subseq
```