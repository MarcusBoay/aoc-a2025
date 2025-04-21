import copy


QUIZ_NUMBER = "21"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        ins = dict()
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split(" => ")
            ins[line[0]] = line[1]
        fp.close()
        print("===", self.fileName, "===")
        # get all flipped/rotations of enhancement rules
        self.ins = ins.copy()
        for rule in ins:
            output = self.ins[rule]
            rule = list(map(list[str], rule.split('/')))
            ruleFlipped = []
            for line in rule:
                lineFlipped = line[:]
                lineFlipped.reverse()
                ruleFlipped.append(lineFlipped[:])

            ruleFlippedStr = []
            for row in ruleFlipped:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            l = len(rule)
            # rotate unflipped rule
            rotatedPrev = copy.deepcopy(rule)
            rotated = copy.deepcopy(rotatedPrev)
            for i in range(l):
                for j in range(l):
                    rotated[i][j] = rotatedPrev[l-j-1][i]
            ruleFlippedStr = []
            for row in rotated:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            rotatedPrev = copy.deepcopy(rotated)
            for i in range(l):
                for j in range(l):
                    rotated[i][j] = rotatedPrev[l-j-1][i]
            ruleFlippedStr = []
            for row in rotated:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            rotatedPrev = copy.deepcopy(rotated)
            for i in range(l):
                for j in range(l):
                    rotated[i][j] = rotatedPrev[l-j-1][i]
            ruleFlippedStr = []
            for row in rotated:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            rotatedPrev = copy.deepcopy(rotated)
            # rotate flipped rule
            rotatedPrev = copy.deepcopy(ruleFlipped)
            rotated = copy.deepcopy(rotatedPrev)
            for i in range(l):
                for j in range(l):
                    rotated[i][j] = rotatedPrev[l-j-1][i]
            ruleFlippedStr = []
            for row in rotated:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            rotatedPrev = copy.deepcopy(rotated)
            for i in range(l):
                for j in range(l):
                    rotated[i][j] = rotatedPrev[l-j-1][i]
            ruleFlippedStr = []
            for row in rotated:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            rotatedPrev = copy.deepcopy(rotated)
            for i in range(l):
                for j in range(l):
                    rotated[i][j] = rotatedPrev[l-j-1][i]
            ruleFlippedStr = []
            for row in rotated:
                ruleFlippedStr.append("".join(row))
            if "/".join(ruleFlippedStr) not in self.ins:
                self.ins["/".join(ruleFlippedStr)] = output
            rotatedPrev = copy.deepcopy(rotated)

    def solve1(self):
        print("--- Part One ---")
        l = 3 # current length of grid
        n = 0 # current iteration count
        grid = [['.' for i in range(l)] for j in range(l)]
        # starting pattern
        grid[0][1] = '#'
        grid[1][2] = '#'
        grid[2][0] = '#'
        grid[2][1] = '#'
        grid[2][2] = '#'
        while n < 5:
            n += 1
            # get next grid length
            ln = l
            if l % 2 == 0:
                ln += l//2
            else:
                ln += l//3
            # print(n+1, ln)
            # get next grid
            nextGrid = [['.' for i in range(ln)] for j in range(ln)]
            if l % 2 == 0:
                for i in range(0, l, 2):
                    for j in range(0, l, 2):
                        square = "".join(grid[i][j:j+2]) + '/' + "".join(grid[i+1][j:j+2])
                        output = self.ins[square]
                        output = list(map(list[str], output.split('/')))
                        nextGrid[i//2*3][j//2*3] = output[0][0]
                        nextGrid[i//2*3][j//2*3+1] = output[0][1]
                        nextGrid[i//2*3][j//2*3+2] = output[0][2]
                        nextGrid[i//2*3+1][j//2*3] = output[1][0]
                        nextGrid[i//2*3+1][j//2*3+1] = output[1][1]
                        nextGrid[i//2*3+1][j//2*3+2] = output[1][2]
                        nextGrid[i//2*3+2][j//2*3] = output[2][0]
                        nextGrid[i//2*3+2][j//2*3+1] = output[2][1]
                        nextGrid[i//2*3+2][j//2*3+2] = output[2][2]
            else:
                for i in range(0, l, 3):
                    for j in range(0, l, 3):
                        square = "".join(grid[i][j:j+3]) + '/' + "".join(grid[i+1][j:j+3]) + '/' + "".join(grid[i+2][j:j+3])
                        output = self.ins[square]
                        output = list(map(list[str], output.split('/')))
                        nextGrid[i//3*4][j//3*4] = output[0][0]
                        nextGrid[i//3*4][j//3*4+1] = output[0][1]
                        nextGrid[i//3*4][j//3*4+2] = output[0][2]
                        nextGrid[i//3*4][j//3*4+3] = output[0][3]
                        nextGrid[i//3*4+1][j//3*4] = output[1][0]
                        nextGrid[i//3*4+1][j//3*4+1] = output[1][1]
                        nextGrid[i//3*4+1][j//3*4+2] = output[1][2]
                        nextGrid[i//3*4+1][j//3*4+3] = output[1][3]
                        nextGrid[i//3*4+2][j//3*4] = output[2][0]
                        nextGrid[i//3*4+2][j//3*4+1] = output[2][1]
                        nextGrid[i//3*4+2][j//3*4+2] = output[2][2]
                        nextGrid[i//3*4+2][j//3*4+3] = output[2][3]
                        nextGrid[i//3*4+3][j//3*4] = output[3][0]
                        nextGrid[i//3*4+3][j//3*4+1] = output[3][1]
                        nextGrid[i//3*4+3][j//3*4+2] = output[3][2]
                        nextGrid[i//3*4+3][j//3*4+3] = output[3][3]
            grid = nextGrid
            l = ln
            # print(n, grid)
        # print(grid)
        totalLitPixels = 0
        for row in grid:
            for c in row:
                if c == '#':
                    totalLitPixels += 1
        print(f"Number of lit pixels: {totalLitPixels}")

    def solve2(self):
        print("--- Part Two ---")
        l = 3 # current length of grid
        n = 0 # current iteration count
        grid = [['.' for i in range(l)] for j in range(l)]
        # starting pattern
        grid[0][1] = '#'
        grid[1][2] = '#'
        grid[2][0] = '#'
        grid[2][1] = '#'
        grid[2][2] = '#'
        while n < 18:
            n += 1
            # get next grid length
            ln = l
            if l % 2 == 0:
                ln += l//2
            else:
                ln += l//3
            # print(n+1, ln)
            # get next grid
            nextGrid = [['.' for i in range(ln)] for j in range(ln)]
            if l % 2 == 0:
                for i in range(0, l, 2):
                    for j in range(0, l, 2):
                        square = "".join(grid[i][j:j+2]) + '/' + "".join(grid[i+1][j:j+2])
                        output = self.ins[square]
                        output = list(map(list[str], output.split('/')))
                        nextGrid[i//2*3][j//2*3] = output[0][0]
                        nextGrid[i//2*3][j//2*3+1] = output[0][1]
                        nextGrid[i//2*3][j//2*3+2] = output[0][2]
                        nextGrid[i//2*3+1][j//2*3] = output[1][0]
                        nextGrid[i//2*3+1][j//2*3+1] = output[1][1]
                        nextGrid[i//2*3+1][j//2*3+2] = output[1][2]
                        nextGrid[i//2*3+2][j//2*3] = output[2][0]
                        nextGrid[i//2*3+2][j//2*3+1] = output[2][1]
                        nextGrid[i//2*3+2][j//2*3+2] = output[2][2]
            else:
                for i in range(0, l, 3):
                    for j in range(0, l, 3):
                        square = "".join(grid[i][j:j+3]) + '/' + "".join(grid[i+1][j:j+3]) + '/' + "".join(grid[i+2][j:j+3])
                        output = self.ins[square]
                        output = list(map(list[str], output.split('/')))
                        nextGrid[i//3*4][j//3*4] = output[0][0]
                        nextGrid[i//3*4][j//3*4+1] = output[0][1]
                        nextGrid[i//3*4][j//3*4+2] = output[0][2]
                        nextGrid[i//3*4][j//3*4+3] = output[0][3]
                        nextGrid[i//3*4+1][j//3*4] = output[1][0]
                        nextGrid[i//3*4+1][j//3*4+1] = output[1][1]
                        nextGrid[i//3*4+1][j//3*4+2] = output[1][2]
                        nextGrid[i//3*4+1][j//3*4+3] = output[1][3]
                        nextGrid[i//3*4+2][j//3*4] = output[2][0]
                        nextGrid[i//3*4+2][j//3*4+1] = output[2][1]
                        nextGrid[i//3*4+2][j//3*4+2] = output[2][2]
                        nextGrid[i//3*4+2][j//3*4+3] = output[2][3]
                        nextGrid[i//3*4+3][j//3*4] = output[3][0]
                        nextGrid[i//3*4+3][j//3*4+1] = output[3][1]
                        nextGrid[i//3*4+3][j//3*4+2] = output[3][2]
                        nextGrid[i//3*4+3][j//3*4+3] = output[3][3]
            grid = nextGrid
            l = ln
            # print(n, grid)
        # print(grid)
        totalLitPixels = 0
        for row in grid:
            for c in row:
                if c == '#':
                    totalLitPixels += 1
        print(f"Number of lit pixels: {totalLitPixels}")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
