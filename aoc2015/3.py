QUIZ_NUMBER = "3"

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
        been = dict()
        x, y = 0, 0
        been[(x, y)] = 1
        for m in self.ins:
            if m == '^':
                y -= 1
            elif m == 'v':
                y += 1
            elif m == '<':
                x -= 1
            elif m == '>':
                x += 1
            if (x, y) not in been:
                been[(x, y)] = 0
            been[(x, y)] += 1
        print("Number of houses that received at least one present:", len(been))

    def solve2(self):
        print("--- Part Two ---")
        been = dict()
        x1, y1, x2, y2 = 0, 0, 0, 0
        been[(0, 0)] = 2
        for i in range(0, len(self.ins), 2):
            # santa
            m = self.ins[i]
            if m == '^':
                y1 -= 1
            elif m == 'v':
                y1 += 1
            elif m == '<':
                x1 -= 1
            elif m == '>':
                x1 += 1
            if (x1, y1) not in been:
                been[(x1, y1)] = 0
            been[(x1, y1)] += 1
            # robo-santa
            m = self.ins[i+1]
            if m == '^':
                y2 -= 1
            elif m == 'v':
                y2 += 1
            elif m == '<':
                x2 -= 1
            elif m == '>':
                x2 += 1
            if (x2, y2) not in been:
                been[(x2, y2)] = 0
            been[(x2, y2)] += 1
        print("Number of houses that received at least one present with Robo-Santa:", len(been))

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
