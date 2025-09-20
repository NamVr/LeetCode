class Router:

    def __init__(self, memoryLimit: int):
        self.mp = {} # track duplicates
        self.queue = deque() # FIFO packets
        self.timestamp = {} # timestamp tracking
        self.st = {}
        self.maxSize = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.mp:
            return False # no need to add duplicate packet.
        
        if len(self.queue) == self.maxSize:
            res = self.queue.popleft()
            del self.mp[res]
            self.st[res[1]] = self.st.get(res[1], 0) + 1
        
        self.queue.append(packet)
        self.mp[packet] = 1

        if destination not in self.timestamp:
            self.timestamp[destination] = []
        self.timestamp[destination].append(timestamp)
        
        return True
        

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        
        res = self.queue.popleft()
        del self.mp[res]
        self.st[res[1]] = self.st.get(res[1], 0) + 1
        return list(res)


    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.timestamp:
            return 0
        
        p = self.timestamp[destination]
        temp = self.st.get(destination, 0)
        right = bisect.bisect_left(p, startTime, temp)
        left = bisect.bisect_right(p, endTime, temp)
        return left - right


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
