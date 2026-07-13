class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        sortedPosSpeed = [(p,v) for p,v in sorted(zip(position, speed))]
        prevTime = 0

        for i in range(-1, -len(sortedPosSpeed)-1, -1):
            p, v = sortedPosSpeed[i]
            t = (target - p)/v

            if fleets and t <= prevTime:
                continue
            else:
                fleets += 1
                prevTime = t

        return fleets