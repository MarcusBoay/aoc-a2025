QUIZ_NUMBER = "15"

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
        self.ins = list(map(int, fp.read().split()))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        a = self.ins[0]
        b = self.ins[1]
        af = 16807
        bf = 48271
        d = 2147483647
        finalCount = 0
        for _ in range(40000000):
            a *= af
            a %= d
            b *= bf
            b %= d
            ar = a & 0xFFFF
            br = b & 0xFFFF
            if ar == br:
                finalCount += 1
        print(f"Judge's final count: {finalCount}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
