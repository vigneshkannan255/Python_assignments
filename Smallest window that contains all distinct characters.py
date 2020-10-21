'''Smallest window that contains all distinct characters
This question was asked by Microsoft, Amazon and DailyHunt.
You are given a string. You have to find the smallest substring which contains all the distinct characters of the given string.
Follow Up: Try solving this question in O(n), using the sliding window technique.
Input format:
The first and only line of input contains a string. The length of string lies in the range: [1, 10000].
Constraints:
Time limit: 1 second
Output format:
The first and only line of output contains the smallest substring with all the distinct characters of given substring. If there are two or more substrings of same length, then print the one with smallest starting index.  
Sample Input:
aaab
Sample Output:
ab
Explanation:
ab of length 2 is the smallest window with highest number of distinct characters.'''

Solution:
s=input()
s1=list(set(s))
s1.sort()
r=s
for i in range(len(s)):
    for j in range(i+1,len(s)):
        v=list(s[i:j])
        v.sort()
        if v==s1:
            if len(s[i:j])<=len(r):
                r=s[i:j]
print(r)                
        
        
    
