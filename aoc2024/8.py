QUIZ_NUMBER = "8"

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
            self.ins.append(list(map(str, (arr[i]))))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        pos = dict()
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                antenna = self.ins[i][j]
                if antenna != '.':
                    if antenna not in pos:
                        pos[antenna] = []
                    pos[antenna].append((i, j))

        antinodeMap = [['.' for j in range(len(self.ins[0]))] for i in range(len(self.ins))]
        for antenna in pos:
            for pi1 in range(len(pos[antenna])):
                for pi2 in range(pi1+1, len(pos[antenna])):
                    # pi1 <-d-> pi2
                    di = pos[antenna][pi2][0] - pos[antenna][pi1][0]
                    dj = pos[antenna][pi2][1] - pos[antenna][pi1][1]
                    # X <-d-> pi1 <-d-> pi2
                    i = pos[antenna][pi1][0] - di
                    j = pos[antenna][pi1][1] - dj
                    if 0 <= i < len(self.ins) and 0 <= j < len(self.ins[i]):
                        antinodeMap[i][j] = '#'
                    # pi1 <-d-> pi2 <-d-> X
                    i = pos[antenna][pi2][0] + di
                    j = pos[antenna][pi2][1] + dj
                    if 0 <= i < len(self.ins) and 0 <= j < len(self.ins[i]):
                        antinodeMap[i][j] = '#'

        uniqueLocations = 0
        for line in antinodeMap:
            for c in line:
                if c == '#':
                    uniqueLocations += 1
        print("Number of unique locations of antinodes:", uniqueLocations)

    def solve2(self):
        print("--- Part Two ---")
        pos = dict()
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                antenna = self.ins[i][j]
                if antenna != '.':
                    if antenna not in pos:
                        pos[antenna] = []
                    pos[antenna].append((i, j))

        antinodeMap = [['.' for j in range(len(self.ins[0]))] for i in range(len(self.ins))]
        for antenna in pos:
            for pi1 in range(len(pos[antenna])):
                for pi2 in range(pi1+1, len(pos[antenna])):
                    antinodeMap[pos[antenna][pi1][0]][pos[antenna][pi1][1]] = '#'
                    antinodeMap[pos[antenna][pi2][0]][pos[antenna][pi2][1]] = '#'
                    # pi1 <-d-> pi2
                    di = pos[antenna][pi2][0] - pos[antenna][pi1][0]
                    dj = pos[antenna][pi2][1] - pos[antenna][pi1][1]
                    # X <-d-> pi1 <-d-> pi2
                    i = pos[antenna][pi1][0] - di
                    j = pos[antenna][pi1][1] - dj
                    while 0 <= i < len(self.ins) and 0 <= j < len(self.ins[i]):
                        antinodeMap[i][j] = '#'
                        i -= di
                        j -= dj
                    # pi1 <-d-> pi2 <-d-> X
                    i = pos[antenna][pi2][0] + di
                    j = pos[antenna][pi2][1] + dj
                    while 0 <= i < len(self.ins) and 0 <= j < len(self.ins[i]):
                        antinodeMap[i][j] = '#'
                        i += di
                        j += dj
        # for row in antinodeMap:
        #     print("".join(row))
        uniqueLocations = 0
        for line in antinodeMap:
            for c in line:
                if c == '#':
                    uniqueLocations += 1
        print("Number of unique locations of antinodes:", uniqueLocations)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
