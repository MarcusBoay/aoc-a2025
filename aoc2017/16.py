QUIZ_NUMBER = "16"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in", n=16):
        solution = Solution(fileName, n)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in", 5)

    def __init__(self, fileName, n):
        self.n = n
        self.programs = []
        for i in range(n):
            self.programs.append(chr(ord('a')+i))
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = list(map(str, fp.read().split(',')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        for instr in self.ins:
            if instr[0] == 's':
                spinSize = int(instr[1::])
                while spinSize:
                    self.programs.insert(0, self.programs.pop())
                    spinSize -= 1
            elif instr[0] == 'x':
                p1, p2 = instr[1::].split('/')
                p1, p2 = int(p1), int(p2)
                self.programs[p1], self.programs[p2] = self.programs[p2], self.programs[p1]
            elif instr[0] == 'p':
                p1, p2 = instr[1::].split('/')
                i1, i2 = 0, 0
                for i in range(len(self.programs)):
                    p = self.programs[i]
                    if p == p1:
                        i1 = i
                    elif p == p2:
                        i2 = i
                self.programs[i1], self.programs[i2] = self.programs[i2], self.programs[i1]
        print(f"Order of programs: {"".join(self.programs)}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
