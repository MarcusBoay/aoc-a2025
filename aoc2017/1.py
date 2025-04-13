QUIZ_NUMBER = "1"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = ""
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = list(map(str, fp.read()))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total = 0
        curDigit = self.ins[0]
        for i in range(1, len(self.ins)):
            if self.ins[i] == curDigit:
                total += int(curDigit)
            else:
                curDigit = self.ins[i]
        if self.ins[-1] == self.ins[0]:
            total += int(self.ins[-1])
        print("Solution to captcha:", total)


    def solve2(self):
        print("--- Part Two ---")
        total = 0
        n = len(self.ins)
        for i in range(0, n):
            j = i + n//2
            if self.ins[i%n] == self.ins[j%n]:
                total += int(self.ins[i%n])
        print("Solution to new captcha:", total)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
