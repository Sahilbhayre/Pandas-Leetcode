class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the sum of the longest sequential prefix
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        # Step 2: Convert nums to a set for O(1) lookup speed
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= seq_sum
        ans = seq_sum
        while ans in num_set:
            ans += 1
            
        return ans