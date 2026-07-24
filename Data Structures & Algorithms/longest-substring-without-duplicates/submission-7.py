class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # loop through string
        # check if we have seen that letter before in every subset
        # if we have seen, reset count and reset seen, move pointer over
        #if haven't seen in subset, increment count
        #return maxCount
        l= 0
        maxLen, currLen = 0, 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            currLen +=1
            maxLen = max(maxLen, r - l + 1)
        return maxLen