from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._timeMap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self._timeMap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        output = ""
        key_lists = self._timeMap[key]

        l, r = 0, len(key_lists) - 1

        while l <= r:
            mid = (l + r) // 2

            if key_lists[mid][1] > timestamp:
                r = mid - 1

            elif key_lists[mid][1] <= timestamp:
                l = mid + 1
                output = key_lists[mid][0]
        
        return output
