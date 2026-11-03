class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set(nums)
        if len(nums) != len(result):
            return True
        return False