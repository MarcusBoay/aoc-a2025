QUIZ_NUMBER = "19"

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
        self.ins = int(fp.read())
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        twoN = 1
        r = self.ins
        while r:
            r >>= 1
            twoN <<= 1
        twoN >>= 1
        r = self.ins - twoN
        winningElf = (r << 1) + 1
        print(f"Elf that gets all the presents: {winningElf}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
