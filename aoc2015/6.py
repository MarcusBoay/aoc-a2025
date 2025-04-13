QUIZ_NUMBER = "6"

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
            line = arr[i].split()
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        grid = [[0 for i in range(1000)] for j in range(1000)]
        for instr in self.ins:
            for i in range(int(instr[1]), int(instr[3])+1):
                for j in range(int(instr[2]), int(instr[4])+1):
                    if instr[0] == "on":
                        grid[i][j] = 1
                    elif instr[0] == "toggle":
                        grid[i][j] ^= 1
                    elif instr[0] == "off":
                        grid[i][j] = 0

        lightsLit = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                lightsLit += grid[i][j]
        print("Number of lit lights:", lightsLit)

    def solve2(self):
        print("--- Part Two ---")
        grid = [[0 for i in range(1000)] for j in range(1000)]
        for instr in self.ins:
            for i in range(int(instr[1]), int(instr[3])+1):
                for j in range(int(instr[2]), int(instr[4])+1):
                    if instr[0] == "on":
                        grid[i][j] += 1
                    elif instr[0] == "toggle":
                        grid[i][j] += 2
                    elif instr[0] == "off":
                        if grid[i][j] > 0:
                            grid[i][j] -= 1

        totalBrightness = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                totalBrightness += grid[i][j]
        print("Total brightness:", totalBrightness)

def main():
    Solution.test()
    Solution.run("6.ex2.in")
    Solution.run()

if __name__ == "__main__":
    main()
