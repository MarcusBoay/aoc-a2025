QUIZ_NUMBER = "9"

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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = list(map(int, arr[i].split()))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self, reverseList = False):
        if not reverseList:
            print("--- Part One ---")
        nextValues = []
        for history in self.ins:
            curDiffs = []
            if not reverseList:
                curDiffs.append(history[::])
            else:
                curDiffs.append(list(reversed(history[::])))

            # get differences at each step
            isZeros = False
            while not isZeros:
                curDiff = []
                isZeros = True
                for i in range(len(curDiffs[-1])-1):
                    d = curDiffs[-1][i+1]-curDiffs[-1][i]
                    curDiff.append(d)
                    if d != 0:
                        isZeros = False
                curDiffs.append(curDiff)

            # get extrapolated value
            i = len(curDiffs)-1
            curDiffs[i].append(0)
            while i > 0:
                curDiffs[i-1].append(curDiffs[i-1][-1]+curDiffs[i][-1])
                i -= 1
            nextValues.append(curDiffs[0][-1])
        print("Sum of extrapolated values:", sum(nextValues))

    def solve2(self):
        print("--- Part Two ---")
        self.solve1(True)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
