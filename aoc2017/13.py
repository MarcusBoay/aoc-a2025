QUIZ_NUMBER = "13"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = dict()
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split(": ")
            self.ins[int(line[0])] = int(line[1])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        totalSeverity = 0
        scanners = dict()
        maxScanner = 0
        for row in self.ins:
            scanners[row] = [0, 'D']
            maxScanner = max(maxScanner, row)
        for ps in range(maxScanner+1):
            if ps in scanners and scanners[ps][0] == 0:
                totalSeverity += self.ins[ps] * ps
            for s in scanners:
                # change directions if at edge
                if scanners[s][0] == self.ins[s]-1:
                    scanners[s][1] = 'U'
                elif scanners[s][0] == 0:
                    scanners[s][1] = 'D'
                # move scanner
                if scanners[s][1] == 'U':
                    scanners[s][0] -= 1
                elif scanners[s][1] == 'D':
                    scanners[s][0] += 1

        print(f"Total severity of the whole trip: {totalSeverity}")

    def solve2(self):
        print("--- Part Two ---")
        scanners = dict()
        maxScanner = 0
        for row in self.ins:
            scanners[row] = 2*(self.ins[row]-1) # time taken to go and come back to 0
            maxScanner = max(maxScanner, row)
        delay = -1
        caught = True
        while caught:
            caught = False
            delay += 1
            for s in scanners:
                if s == 0 and delay == 0:
                    caught = True
                    break
                if ((s+delay) % scanners[s]) == 0:
                    caught = True
                    break
        if not caught:
            print(f"Fewest number of picosends to delay without getting caught: {delay}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
