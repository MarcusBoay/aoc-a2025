QUIZ_NUMBER = "1"

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
        floor = 0
        for c in self.ins:
            if c == '(':
                floor += 1
            else:
                floor -= 1
        print("Resulting floor:", floor)

    def solve2(self):
        print("--- Part Two ---")
        floor = 0
        for i in range(len(self.ins)):
            if self.ins[i] == '(':
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                print("Santa will first enter the basement at position", i+1)
                return

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
