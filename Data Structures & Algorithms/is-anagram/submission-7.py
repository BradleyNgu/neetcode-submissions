class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = {}
        for i in s:
            set1[i] = set1.get(i,0) + 1
        set2 = {}
        for j in t:
            set2[j] = set2.get(j,0) + 1
        return set1 == set2
        