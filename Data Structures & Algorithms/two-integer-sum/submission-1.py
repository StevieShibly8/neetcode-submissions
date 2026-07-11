class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexVal = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in indexVal:
                return [indexVal[diff], i]
            indexVal[v] = i