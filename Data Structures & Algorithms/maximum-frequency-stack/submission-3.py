class FreqStack:

    def __init__(self):
        self.count = 0
        self.stacks = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq
        if freq > len(self.stacks):
            self.stacks.append([])
        self.stacks[freq - 1].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.freq[val] -= 1
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()