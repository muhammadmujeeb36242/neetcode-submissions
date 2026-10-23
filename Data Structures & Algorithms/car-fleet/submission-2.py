class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        time = [(target-p)/s for p,s in cars]
        count = 1
        slowest = time[0]
        for i in range(len(time)):
            if i!=0:
                if time[i] > slowest:
                    count+=1
                    slowest = time[i]
        return count
