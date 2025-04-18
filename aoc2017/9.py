QUIZ_NUMBER = "9"

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
        def backtrack(row):
            x = 0
            ignore = False
            while self.i < len(row):
                c = row[self.i]
                if not ignore and c == '{':
                    self.i += 1
                    x += backtrack(row)
                elif not ignore and c == '}':
                    self.score += x + 1
                    self.i += 1
                    return x + 1
                elif not ignore and c == '<':
                    self.i += 1
                    ignore = True
                elif c == '>':
                    self.i += 1
                    ignore = False
                elif c == '!':
                    self.i += 2
                else:
                    self.i += 1
            return x
        for row in self.ins:
            self.i = 0
            self.score = 0
            backtrack(row)
            print(f"Total score: {self.score}")

    def solve2(self):
        print("--- Part Two ---")
        def backtrack(row):
            x = 0
            ignore = False
            while self.i < len(row):
                c = row[self.i]
                if not ignore and c == '{':
                    self.i += 1
                    x += backtrack(row)
                elif not ignore and c == '}':
                    self.score += x + 1
                    self.i += 1
                    return x + 1
                elif not ignore and c == '<':
                    self.i += 1
                    ignore = True
                elif c == '>':
                    self.i += 1
                    ignore = False
                elif c == '!':
                    self.i += 2
                else:
                    if ignore == True:
                        self.garbage += 1
                    self.i += 1
            return x
        for row in self.ins:
            self.i = 0
            self.score = 0
            self.garbage = 0
            backtrack(row)
            print(f"Total non-cancelled characters within garbage: {self.garbage}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
