QUIZ_NUMBER = "3"
import re

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
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        matches = re.findall(r"mul\((\d+),(\d+)\)", self.ins)
        result = 0
        for match in matches:
            result += int(match[0]) * int(match[1])
        print("Result:", result)

    def solve2(self):
        print("--- Part Two ---")
        dontIter = re.finditer(r"don't\(\)", self.ins)
        doIter = re.finditer(r"do\(\)", self.ins)
        mulIter = re.finditer(r"mul\((\d+),(\d+)\)", self.ins)
        dont = []
        do = []
        while True:
            try:
                dont.append(next(dontIter).start())
            except:
                break
        while True:
            try:
                do.append(next(doIter).start())
            except:
                break
        banned = []
        dontI = 0
        doI = 0
        i = 0
        while dontI < len(dont) and doI < len(do):
            # assumptions:
            # - do/don't cannot appear as the first element nor the last element
            curBan = []
            while banned and dontI < len(dont) and banned[-1][1] > dont[dontI]:
                dontI += 1
            curBan = [dont[dontI]]
            while doI < len(do) and curBan[0] > do[doI]:
                doI += 1
            curBan.append(do[doI])
            banned.append(curBan[::])
            doI += 1
            dontI += 1
            i += 1

        result = 0
        while True:
            try:
                m = next(mulIter)
                j = m.start()
                i = 0
                shouldAdd = True
                for i in range(len(banned)):
                    if banned[i][0] < j < banned[i][1]:
                        shouldAdd = False
                        break

                if shouldAdd:
                    result += int(m.group(1)) * int(m.group(2))
            except:
                break
        print("Result of enabled multiplications:", result)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
