class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i, val in enumerate(numbers):
            if (target - val in numbers) and (target - val != val):
                res.append(i+1)
        return res
            
        
