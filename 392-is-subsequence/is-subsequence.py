class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0

        for char in t:
            if i<len(s) and s[i]==char:
                i+=1
        print(i==len(s))
        return i==len(s)
        


obj =Solution()
obj.isSubsequence("abc","Ahbgdc")