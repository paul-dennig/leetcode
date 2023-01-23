class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        self.inputStack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outputStack.pop()

    def peek(self) -> int:
        if (self.outputStack):
            return self.outputStack[-1]
        else:
            while (self.inputStack):
                self.outputStack.append(self.inputStack.pop())
            return self.outputStack[-1]

    def empty(self) -> bool:
        return (self.inputStack == [] and self.outputStack == [])


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
