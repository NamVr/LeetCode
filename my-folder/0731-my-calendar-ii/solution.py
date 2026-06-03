class MyCalendarTwo:
    def __init__(self):
        self.single = []
        self.double = []

    def book(self, startTime: int, endTime: int) -> bool:

        # Would create a triple booking
        for start, end in self.double:
            if startTime < end and endTime > start:
                return False

        # Create new double-booked intervals
        for start, end in self.single:
            if startTime < end and endTime > start:
                self.double.append(
                    (
                        max(startTime, start),
                        min(endTime, end)
                    )
                )

        self.single.append((startTime, endTime))
        return True
