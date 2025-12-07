QUIZ_NUMBER = "12"
import re
import json

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
        matches = re.findall(r"(-?\d+)", self.ins)
        result = 0
        for match in matches:
            result += int(match)
        print("Result:", result)

    def solve2(self):
        print("--- Part Two ---")
        j = json.loads(self.ins)
        def backtrack(j):
            if isinstance(j, str) or isinstance(j, int):
                return j

            if isinstance(j, list) or isinstance(j, dict):
                hasRed = False
                totalSum = 0
                for k in j:
                    r = None
                    if isinstance(j, dict):
                        r = backtrack(j[k])
                    elif isinstance(j, list):
                        r = backtrack(k)
                    if isinstance(r, str) and isinstance(j, dict) and r == "red":
                        hasRed = True
                        break
                    elif isinstance(r, int):
                        totalSum += r
                if not hasRed:
                    return totalSum
        totalSum = backtrack(j)
        print("Result:", totalSum)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
