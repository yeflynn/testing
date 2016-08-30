#!/usr/bin/env python

#  Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
#
# You must use only standard operations of a stack -- which means only push to top,
#  peek/pop from top, size, and is empty operations are valid.
#
# Depending on your language, stack may not be supported natively. You may simulate
#  a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
#
# You may assume that all operations are valid (for example, no pop or peek operations
#  will be called on an empty queue).

# Comment: Optimization available depends on how often push and pop is needed.
# The list re-construction can be in either push or pop.
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        if self.empty():
            return None

        ret = self.stack[0]
        self.stack = self.stack[1:]
        return ret

    # @return an integer
    def peek(self):
        # Error handling
        ret = None
        try:
            ret = self.stack[0]
        except:
            print("Fatal: xxx")
        return ret

    # @return an boolean
    def empty(self):
        return self.stack.empty()


if __name__ == '__main__':
