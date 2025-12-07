QUIZ_NUMBER = "11"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.serialNumber = 0
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.serialNumber = int(fp.read())
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        grid = [[0 for i in range(300)] for j in range(300)]
        for y in range(1, 301):
            for x in range(1, 301):
                rackID = x + 10
                powerLevel = rackID * y
                powerLevel = powerLevel + self.serialNumber
                powerLevel = powerLevel * rackID
                powerLevel = (powerLevel // 100) % 10
                powerLevel = powerLevel - 5
                grid[y-1][x-1] = powerLevel
        maxPower = 0
        maxX, maxY = 0, 0
        for y in range(1, 301-3):
            for x in range(1, 301-3):
                curPower = \
                    (grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1]) + \
                    (grid[y][x-1]   + grid[y][x]   + grid[y][x+1]  ) + \
                    (grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1])
                if curPower > maxPower:
                    maxPower = curPower
                    maxX, maxY = x, y
        print("Largest total power:", maxPower)
        print("Largest 3x3 square:", maxX, maxY)


    def solve2(self):
        print("--- Part Two ---")
        grid = [[0 for i in range(300)] for j in range(300)]
        for y in range(1, 301):
            for x in range(1, 301):
                rackID = x + 10
                powerLevel = rackID * y
                powerLevel = powerLevel + self.serialNumber
                powerLevel = powerLevel * rackID
                powerLevel = (powerLevel // 100) % 10
                powerLevel = powerLevel - 5
                grid[y-1][x-1] = powerLevel
        maxPower = 0
        maxX, maxY, maxSize = 0, 0, 0
        for s in range(1, 301):
            print(s)
            for y in range(0, 301-s):
                for x in range(0, 301-s):
                    curPower = 0
                    for sy in range(y, y+s):
                        for sx in range(x, x+s):
                            curPower += grid[sy][sx]
                            if curPower > maxPower:
                                maxPower = curPower
                                maxX, maxY, maxSize = x, y, s
        print("Largest total power:", maxPower)
        print("Largest square:", maxX, maxY, maxSize)

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
