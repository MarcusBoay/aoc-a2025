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
            line = list(map(int, arr[i].split()))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        numberOfSafeReports = 0
        for report in self.ins:
            isSafe = True
            for i in range(1, len(report)-1):
                if (1 <= abs(report[i] - report[i-1]) <= 3 and \
                    1 <= abs(report[i] - report[i+1]) <= 3) and\
                   ((report[i-1] < report[i] < report[i+1]) or \
                    (report[i-1] > report[i] > report[i+1])):
                    isSafe = True
                else:
                    isSafe = False
                    break
            if isSafe:
                numberOfSafeReports += 1
        print("Number of safe reports:", numberOfSafeReports)

    def solve2(self):
        print("--- Part Two ---")
        numberOfSafeReports = 0
        for report in self.ins:
            badLevels = []
            for i in range(1, len(report)-1):
                if (1 <= abs(report[i] - report[i-1]) <= 3 and \
                    1 <= abs(report[i] - report[i+1]) <= 3) and\
                   ((report[i-1] < report[i] < report[i+1]) or \
                    (report[i-1] > report[i] > report[i+1])):
                    continue
                else:
                    badLevels.append(i)
                    if i >= 0:
                        badLevels.append(i-1)
                    if i < len(report)-1:
                        badLevels.append(i+1)

            isSafe = False
            for b in badLevels:
                newReport = report[::]
                newReport.pop(b)
                isCurSafe = True
                for i in range(1, len(newReport)-1):
                    if (1 <= abs(newReport[i] - newReport[i-1]) <= 3 and \
                        1 <= abs(newReport[i] - newReport[i+1]) <= 3) and\
                        ((newReport[i-1] < newReport[i] < newReport[i+1]) or \
                        (newReport[i-1] > newReport[i] > newReport[i+1])):
                        isCurSafe = True
                    else:
                        isCurSafe = False
                        break
                # we only need one modified report to be safe
                if isCurSafe:
                    isSafe = True
                    break
            if isSafe or not badLevels:
                numberOfSafeReports += 1

        print("Number of safe reports with the Problem Dampener:", numberOfSafeReports)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
