class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        len of strings cant be same

        """

        if len(s) != len(t):
            return False
        
        s_set = {}
        t_set = {}

        for c in s:
            if c in s_set:
                s_set[c] += 1
            else:
                s_set[c] = 0
        for c in t:
            if c in t_set:
                t_set[c] += 1
            else:
                t_set[c] = 0
        
        for c in t_set:
            if c in t_set and c in s_set:
                if t_set[c] != s_set[c]:
                    return False
                else:
                    continue
            elif c in t_set and c not in s_set:
                return False
        return True