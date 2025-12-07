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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            self.ins.append(list(map(int, arr[i].split())))
        fp.close()
        print("===", self.fileName, "===")
        print(self.ins)

    def solve1(self):
        print("--- Part One ---")
        checksum = 0
        for row in self.ins:
            curMin, curMax = row[0], row[0]
            for x in row:
                curMin = min(curMin, x)
                curMax = max(curMax, x)
            checksum += (curMax - curMin)
        print("Checksum:", checksum)

    def solve2(self):
        print("--- Part Two ---")
        checksum = 0
        for row in self.ins:
            found = False
            for i in range(len(row)):
                for j in range(i+1, len(row)):
                    if row[i] <= row[j] and row[j] % row[i] == 0:
                        checksum += row[j] // row[i]
                        found = True
                    elif row[j] <= row[i] and row[i] % row[j] == 0:
                        checksum += row[i] // row[j]
                        found = True
                    if found:
                        break
                if found:
                    break
        print("Checksum:", checksum)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()