class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        sortedPosSpeed = [(p,v) for p,v in sorted(zip(position, speed))]
        print(sortedPosSpeed)

        for i in range(-1, -len(sortedPosSpeed)-1, -1):
            p, v = sortedPosSpeed[i]
            t = (target - p)/v
            print(p,v,t)

            if fleets and t <= fleets[-1]:
                continue
            else:
                fleets.append(t)

        print(fleets)
        return len(fleets)