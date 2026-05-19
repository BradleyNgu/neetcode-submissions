class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bruh = enumerate(nums)
        prev = {}

        for i, n in bruh:
            diff = target - n
            if diff in prev:
                return[prev[diff], i]
            prev[n] = i
            
        