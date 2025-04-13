QUIZ_NUMBER = "7"

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
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        def backtrack(eq, s, i):
            if s == eq[0] and i == len(eq):
                return True
            if i >= len(eq):
                return False
            return backtrack(eq, s+eq[i], i+1) or \
                   backtrack(eq, s*eq[i], i+1)
        totalCalibrationResult = 0
        i = 0
        for equation in self.ins:
            i += 1
            possible = backtrack(equation, equation[1], 2)
            if possible:
                totalCalibrationResult += equation[0]
        print("Total calibration result:", totalCalibrationResult)


    def solve2(self):
        print("--- Part Two ---")
        def backtrack(eq, s, i):
            if s == eq[0] and i == len(eq):
                return True
            if i >= len(eq):
                return False
            m = 10
            while eq[i] % m != eq[i]:
                m *= 10
            r = s * m + eq[i]
            return backtrack(eq, s+eq[i], i+1) or \
                   backtrack(eq, s*eq[i], i+1) or \
                   backtrack(eq, r, i+1)
        totalCalibrationResult = 0
        i = 0
        for equation in self.ins:
            i += 1
            possible = backtrack(equation, equation[1], 2)
            if possible:
                totalCalibrationResult += equation[0]
        print("Total calibration result:", totalCalibrationResult)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
