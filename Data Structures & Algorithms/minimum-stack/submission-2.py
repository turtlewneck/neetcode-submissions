class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = 0 # index of the currently smallest element

    def push(self, val: int) -> None:
        # compare to the stack index of the previously inserted, if its higher, then do not 
        # change the index
        # but first, if there is no stack to begin with, just insert it in
        if self.stack:
            # if not self.stack[self.stack[-1][1]][0]:
            #     self.smallest = 0
            if val < self.stack[self.stack[-1][1]][0]:
                #is smaller, so we need to change the value of the smallest
                self.smallest = len(self.stack)# update to the current index 
                #[3,5,4,0]
                #[0,0,0,3]
        else:
            self.smallest = 0
        self.stack.append((val, self.smallest))
        return None

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.smallest = self.stack[-1][1]
        else:
            self.smallest = 0
        return None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[self.stack[-1][1]][0]
