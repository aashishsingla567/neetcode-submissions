class MinStack:
    def __init__(self):
        self.stack = []
        self.lastMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.lastMin:
            self.lastMin.append(val)
        else:
            self.lastMin.append(min(self.lastMin[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.lastMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lastMin[-1]
