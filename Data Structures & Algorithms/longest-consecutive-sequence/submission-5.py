class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(list(set(nums)))
        count = 0
        maxCount = 0
        print(sortedNums)
        for i in range(len(sortedNums)):
            if i == 0 or sortedNums[i] == sortedNums[i-1] + 1:
                count += 1
            else:
                count = 1
            maxCount = max(maxCount, count)
        return maxCount