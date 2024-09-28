class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0  

        steps = 0
        current_jump = 0
        max_reachable = 0

        for i in range(len(nums) - 1): 
            max_reachable = max(max_reachable, i + nums[i])
            
            if i == current_jump:  
                steps += 1
                current_jump = max_reachable
                
            if current_jump >= len(nums) - 1:  
                break

        return steps
       