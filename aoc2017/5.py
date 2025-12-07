QUIZ_NUMBER = "5"

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
        self.ins = list(map(int, fp.read().split('\n')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        jumpOffsets = self.ins[::]
        step = 0
        i = 0
        while i < len(jumpOffsets):
            j = i + jumpOffsets[i]
            jumpOffsets[i] += 1
            i = j
            step += 1
        print("Steps to exit:", step)


    def solve2(self):
        print("--- Part Two ---")
        jumpOffsets = self.ins[::]
        step = 0
        i = 0
        while i < len(jumpOffsets):
            j = i + jumpOffsets[i]
            if jumpOffsets[i] >= 3:
                jumpOffsets[i] -= 1
            else:
                jumpOffsets[i] += 1
            i = j
            step += 1
        print("Steps to exit:", step)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
