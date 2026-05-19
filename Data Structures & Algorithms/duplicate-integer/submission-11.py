class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bruh = set()
        for i in nums:
            if i in bruh:
                return True
            bruh.add(i)
        return False

        