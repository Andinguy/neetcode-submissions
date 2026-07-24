class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = s.replace("?","")
        d= d.replace(" ", "")
        d= d.replace(",", "")
        d= d.replace("'", "")
        d= d.replace(".", "")
        d= d.replace(":", "")
        l,r = 0, len(d)-1
        for i in range(len(d)):
            if d[l].lower() != d[r].lower():
                return False
            l+=1
            r-=1
        return True    