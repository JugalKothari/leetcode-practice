class RecentCounter:

    def __init__(self):
        self.tlist=[]

    def ping(self, t: int) -> int:
        self.tlist.append(t)
        while self.tlist[0]<t-3000:
            self.tlist.pop(0)
        return len(self.tlist)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
