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
            print("Exception occured!!", e)
        print("Decompressed length of the file:", decompressedLength)

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
