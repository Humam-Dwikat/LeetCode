# from typing import List


class Solution(object):
    def kidsWithCandies(self, candies, extra_candies):
        """
        :type candies: List[int]
        :type extra_candies: int
        :rtype: List[bool]
        """
        results = []
        max_number = max(candies)
        for kid in candies:

            if kid + extra_candies >= max_number:
                results.append(True)
            else:
                results.append(False)

        return results


solution = Solution()
candies = [2, 3, 5, 1, 3]
print(solution.kidsWithCandies(candies=candies, extra_candies=3))
