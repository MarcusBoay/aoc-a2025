QUIZ_NUMBER = "17"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = int(fp.read())
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        b = [0]
        ni = 0
        for i in range(1, 2017+1):
            ni = (ni + self.ins) % len(b)
            ni += 1
            b.insert(ni, i)
        for i in range(len(b)):
            if b[i] == 2017:
                print(f"Value after 2017: {b[i+1]}")
                return

    def solve2(self):
        print("--- Part Two ---")
        ni = 0
        valueAfterZero = 0
        for i in range(1, 50000000+1):
            ni = (ni + self.ins) % i
            ni += 1
            if ni == 1:
                valueAfterZero = i
        print(f"Value after 50000000: {valueAfterZero}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
