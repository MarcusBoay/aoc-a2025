QUIZ_NUMBER = "2"

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
        self.ins = list(map(str, fp.read().split('\n')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        i, j = 0, 0
        code = ""
        for instr in self.ins:
            for move in instr:
                if move ==  'U' and i > 0:
                    i -= 1
                elif move == 'D' and i < 2:
                    i += 1
                elif move == 'L' and j > 0:
                    j -= 1
                elif move == 'R' and j < 2:
                    j += 1
            code += str(keypad[i][j])
        print("Bathroom code:", code)


    def solve2(self):
        print("--- Part Two ---")
        keypad = [
            ['0', '0', '1', '0', '0'],
            ['0', '2', '3', '4', '0'],
            ['5', '6', '7', '8', '9'],
            ['0', 'A', 'B', 'C', '0'],
            ['0', '0', 'D', '0', '0']
        ]
        i, j = 2, 0
        ii, jj = 2, 0
        code = ""
        for instr in self.ins:
            for move in instr:
                ii = i
                jj = j
                if move ==  'U' and i > 0:
                    ii -= 1
                elif move == 'D' and i < 4:
                    ii += 1
                elif move == 'L' and j > 0:
                    jj -= 1
                elif move == 'R' and j < 4:
                    jj += 1

                if keypad[ii][jj] != '0':
                    i = ii
                    j = jj
            code += keypad[i][j]
        print("Bathroom code:", code)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
