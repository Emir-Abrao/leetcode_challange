class SummaryRanges:
    def __init__(self):
        self.seen = [False] * 10001  # indices 0..10000 inclusive

    def addNum(self, value: int) -> None:
        self.seen[value] = True

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        i = 0
        while i <= 10000:
            if self.seen[i]:
                start = i
                while i <= 10000 and self.seen[i]:
                    i += 1
                end = i - 1
                intervals.append([start, end])
            else:
                i += 1
        return intervals