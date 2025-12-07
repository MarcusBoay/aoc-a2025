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
        self.ins = list(map(str, fp.read().split('\n')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        totalChars = 0
        totalMemChars = 0
        # 0 = not hexadecimal char
        # 1 = is hexadecimal char (at 'x')
        # 2 = is hexadecimal char (at first digit in hex char)
        isHex = 0
        # 0 = not esc char
        # 1 = esc char (at '\')
        isEsc = 0
        for s in self.ins:
            totalChars += len(s)
            curChars = len(s)
            curMemChars = 0
            for i in range(1, len(s)-1):
                if not isEsc and s[i] != '\\':
                    curMemChars += 1
                elif not isEsc and s[i] == '\\':
                    isEsc = 1
                elif isEsc and s[i] == '\\':
                    curMemChars += 1
                    isEsc = 0
                elif isEsc and s[i] == '\"':
                    curMemChars += 1
                    isEsc = 0
                elif isEsc and s[i] == 'x':
                    isHex = 1
                elif isEsc and isHex == 1:
                    isHex = 2
                elif isEsc and isHex == 2:
                    curMemChars += 1
                    isEsc = 0
                    isHex = 0
            totalMemChars += curMemChars
            # print("cur string:", s, curChars, curMemChars)
        print("Result:", totalChars - totalMemChars)


    def solve2(self):
        print("--- Part Two ---")
        totalChars = 0
        totalMemChars = 0
        for s in self.ins:
            totalChars += len(s)
            curChars = len(s)
            curMemChars = 2
            for i in range(0, len(s)):
                if s[i] == '\"':
                    curMemChars += 1
                elif s[i] == '\\':
                    curMemChars += 1
                curMemChars += 1
            totalMemChars += curMemChars
            # print("cur string:", s, curChars, curMemChars)
        print("Result:", totalMemChars - totalChars)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
