class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] #first subarray will be first element
        currentsum = 0

        for n in nums:
            if currentsum < 0:
                currentsum = 0 #negative values are redundant in sum
            currentsum += n
            maxSub = max(currentsum, maxSub)
