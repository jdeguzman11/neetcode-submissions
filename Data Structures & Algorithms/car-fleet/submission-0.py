class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for position, speed in cars:
            time = (target - position) / speed
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)
