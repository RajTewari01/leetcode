'''
answer.py -- two-sum.py
'''

from typing import List, Optional

class Solution:
    def twoSum(
        self,
        nums: List[int],
        target: int
    ) -> Optional[List[int]]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [None,None]

print(Solution().twoSum([2,7,11,15],9))