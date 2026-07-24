class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sSet = set()
        l = 0
        for c in range(len(s)):
            while s[c] in sSet:
                sSet.remove(s[l])
                l +=1
            longest = max(longest, (c - l)+1)
            sSet.add(s[c])
            
        return longest

