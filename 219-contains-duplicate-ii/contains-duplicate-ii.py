class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        iteration_map = {}
        for i, num in enumerate(nums):

            if num in iteration_map and (i - iteration_map[num]) <= k:
                return True
            iteration_map[num] = i

        return False
