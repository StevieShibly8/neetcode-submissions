class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1

        return heapq.nlargest(k, res, key=res.get)