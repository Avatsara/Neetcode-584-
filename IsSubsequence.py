class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        fp,sp=0,0
        n = len(s) 
        p = len(t)
        while fp<n and sp<p:  
            if s[fp]==t[sp]:   
                fp+=1 
        
            sp+=1
        return fp==n
