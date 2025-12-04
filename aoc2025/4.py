QUIZ_NUMBER = "4"

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
        for i in range(0, len(arr)-1):
            line = list(arr[i])
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total = self.totalAccessibleRolls()
        print(f"Number of rolls of accessible: {total}")

    def totalAccessibleRolls(self) -> int:
        total = 0
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                if self.ins[i][j] == '.':
                    continue
                allNext = [(i-1, j), (i-1, j+1), (i,j+1), (i+1,j+1), \
                           (i+1, j), (i+1, j-1), (i, j-1), (i-1, j-1)]
                adjacent = 0
                for ni, nj in allNext:
                    if ni < 0 or ni >= len(self.ins) or \
                        nj < 0 or nj >= len(self.ins[i]):
                        continue
                    # print(ni, len(self.ins), nj, len(self.ins[i]))
                    # print(self.ins[ni])
                    if self.ins[ni][nj] == '@' or self.ins[ni][nj] == 'x':
                        adjacent += 1
                if adjacent < 4:
                    total += 1
                    self.ins[i][j] = 'x'
        return total


    def solve2(self):
        print("--- Part Two ---")
        total_removed = 0
        while True:
            cur_removed = self.totalAccessibleRolls() 
            for i in range(len(self.ins)):
                for j in range(len(self.ins[i])):
                    if self.ins[i][j] == 'x':
                        self.ins[i][j] = '.'
            if cur_removed == 0:
                break
            else:
                total_removed += cur_removed
        print(f"Total rolls removed: {total_removed}")


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
