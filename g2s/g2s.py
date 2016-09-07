#!/usr/bin/env python
# MIT LICENSE DO WHATEVER YOU WANT
# Author: Calvin Ference

# Data will come in as in the following input
data = '''
'''


def main():
    global data
    f = open("asgore.txt", "r")
    data = f.readlines()

class Block(object):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def next(self):
        if len(self.data) <= 0:
            raise StopIteration
        else:
            extra_lines = []
            block = []
            for n in xrange(len(self.data)):
                if self.data[n][0] == "E":
                    block = self.data[n:n+6]
                    self.data = self.data[n+6:]
                    break
                else:
                    extra_lines.append(self.data[n])
            return (extra_lines, block, self.data )

# Return will be all the "extra" lines, the new block, the remaining data
def getNextBlock(data):
    extra_lines = []
    block = []
    remaining = []
    for n in xrange(len(data)):
        if data[n][0] == "E":
            block = data[n:n+6]
            remaining = data[n+6:]
            break
        else:
            extra_lines.append(data[n])
    return (extra_lines, block, remaining)



if __name__ == "__main__":
    main()
