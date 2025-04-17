QUIZ_NUMBER = "18"

class Solution:
    def run(n=100, fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(n, fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(5, QUIZ_NUMBER + ".ex.in")

    def __init__(self, n, fileName):
        self.n = n
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = list(map(str, arr[i]))
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")
        self.ins_copy = self.ins[:]

    def getNeighbors(self, i, j):
        total = 0
        if i > 0 and self.ins[i-1][j] == '#':
            total += 1
        if i > 0 and j < len(self.ins[i])-1 and self.ins[i-1][j+1] == '#':
            total += 1
        if j < len(self.ins[i])-1 and self.ins[i][j+1] == '#':
            total += 1
        if i < len(self.ins)-1 and j < len(self.ins[i])-1 and self.ins[i+1][j+1] == '#':
            total += 1
        if i < len(self.ins)-1 and self.ins[i+1][j] == '#':
            total += 1
        if i < len(self.ins)-1 and j > 0 and self.ins[i+1][j-1] == '#':
            total += 1
        if j > 0 and self.ins[i][j-1] == '#':
            total += 1
        if i > 0 and j > 0 and self.ins[i-1][j-1] == '#':
            total += 1
        return total

    def getTotalLit(self):
        totalLit = 0
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                if self.ins[i][j] == '#':
                    totalLit += 1
        print(f"Number of lights lit after {self.n} steps: {totalLit}")

    def solve1(self):
        print("--- Part One ---")
        self.ins = self.ins_copy[:]
        for s in range(self.n):
            nextIns = []
            for i in range(len(self.ins)):
                nextRow = []
                for j in range(len(self.ins[i])):
                    neighbors = self.getNeighbors(i, j)
                    if self.ins[i][j] == '#' and neighbors == 2 or neighbors == 3:
                        nextRow.append('#')
                    elif self.ins[i][j] == '.' and neighbors == 3:
                        nextRow.append('#')
                    else:
                        nextRow.append('.')
                nextIns.append(nextRow[:])
            self.ins = nextIns[:]
        self.getTotalLit()

    def solve2(self):
        print("--- Part Two ---")
        self.ins = self.ins_copy[:]
        self.ins[0][0] = '#'
        self.ins[0][len(self.ins[0])-1] = '#'
        self.ins[len(self.ins)-1][len(self.ins[0])-1] = '#'
        self.ins[len(self.ins)-1][0] = '#'

        for s in range(self.n):
            nextIns = []
            for i in range(len(self.ins)):
                nextRow = []
                for j in range(len(self.ins[i])):
                    neighbors = self.getNeighbors(i, j)
                    if (i == 0 and j == 0) or \
                        (i == 0 and j == len(self.ins[i])-1) or \
                        (i == len(self.ins)-1 and j == len(self.ins[i])-1) or \
                        (i == len(self.ins)-1 and j == 0):
                        nextRow.append('#')
                    elif self.ins[i][j] == '#' and neighbors == 2 or neighbors == 3:
                        nextRow.append('#')
                    elif self.ins[i][j] == '.' and neighbors == 3:
                        nextRow.append('#')
                    else:
                        nextRow.append('.')
                nextIns.append(nextRow[:])
            self.ins = nextIns[:]
        self.getTotalLit()


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
