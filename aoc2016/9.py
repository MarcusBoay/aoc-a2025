QUIZ_NUMBER = "9"
import re

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        decompressedLength = len(self.ins)
        mIter = re.finditer(r"\((\d+)x(\d+)\)", self.ins)
        try:
            curStart, curEnd = 0, 0
            prevLength = 0
            while True:
                m = next(mIter)
                nextEnd = m.end()
                if nextEnd > curEnd + prevLength:
                    # remove marker from length
                    curStart, curEnd = m.start(), m.end()
                    decompressedLength -= curEnd - curStart

                    # add n * reps-1 for the decompressed section
                    n = int(m.group(1))
                    reps = int(m.group(2))
                    prevLength = n
                    decompressedLength += n*(reps-1)

                    # print(m, prevDecompressedLength, decompressedLength)

        except Exception as e:
            pass
            # print("Exception occured!!", e)
        print("Decompressed length of the file:", decompressedLength)

    def solve2(self):
        print("--- Part Two ---")

        decompressedLength = len(self.ins)
        mIter = re.finditer(r"\((\d+)x(\d+)\)", self.ins)
        self.arr = []
        try:
            while True:
                m = next(mIter)
                self.arr.append((m.start(), m.end(), int(m.group(1)), int(m.group(2))))
        except Exception as e:
            pass
            # print("Exception occured!!", e)

        self.i = 0
        self.takeaway = 0
        def backtrack():
            s = self.arr[self.i][0]
            e = self.arr[self.i][1]
            l = self.arr[self.i][2]
            rep = self.arr[self.i][3]

            t = 0
            while self.i+1 < len(self.arr) and self.arr[self.i+1][0] < e+l:
                self.i += 1
                t += backtrack()

            if t == 0:
                # print(self.i, s, e, l, rep, l*rep)
                self.takeaway += l + (e-s)
                return l*rep
            # print(self.i, s, e, l, rep, t+rep)
            self.takeaway += (e-s)
            return t*rep
        expandedLengths = 0
        while self.i < len(self.arr):
            expandedLengths += backtrack()
            self.i += 1
        decompressedLength = expandedLengths + decompressedLength - self.takeaway
        print("Decompressed length of the file:", decompressedLength)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
