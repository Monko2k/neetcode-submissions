class FreqStack:

    def __init__(self):
        self.count = 0
        self.stacks = {}
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq

        if freq in self.stacks and len(self.stacks[freq]) > 0:
            self.stacks[freq].append(val)
        else:
            self.stacks[freq] = [val]
            self.count += 1

    def pop(self) -> int:
        val = self.stacks[self.count].pop()
        self.freq[val] -= 1
        if len(self.stacks[self.count]) == 0:
            self.count -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()