class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = nums[0]

        # # Single element
        # if len(nums) == 1:
        #     return nums[0]

        # # Check all single elements
        # for k in range(len(nums)):
        #     if nums[k] > s:
        #         s = nums[k]

        # # Check all subarrays of length 2 and above
        # for i in range(len(nums)):
        #     for j in range(i + 2, len(nums) + 1):  # j is exclusive end
        #         check = sum(nums[i:j])
        #         if check > s:
        #             s = check

        # return s
    
        max_sum = nums[0]
        current = nums[0]

        for n in nums[1:]:
            current = max(n, current + n)
            max_sum = max(max_sum, current)

        return max_sum

                