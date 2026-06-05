class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevnum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevnum:
                return {prevnum[diff], i}
            prevnum[n] = i 
        return
