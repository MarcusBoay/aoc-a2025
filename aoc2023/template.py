
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
            line = arr[i].split('|')
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
