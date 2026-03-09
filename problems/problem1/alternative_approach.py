'''
alternative_approach.py
'''
import typing 
class Solution:
    def twoSum(
        self,
        nums: typing.List[int],
        target: int
    ) -> typing.Optional[typing.List[int]]:
        seen_number = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen_number:
                return [seen_number[diff], index]
            seen_number[num] = index
        return [None, None]

            

            
        