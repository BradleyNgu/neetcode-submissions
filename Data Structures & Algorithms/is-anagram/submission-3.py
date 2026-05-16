class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        count = {}
        for n in s:
            count[n] = count.get(n,0)+1
        count2 = {}
        for i in t:
            count2[i] = count2.get(i,0)+1
        return count == count2
    





        