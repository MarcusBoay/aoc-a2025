QUIZ_NUMBER = "1"

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
        self.ins = list(map(str, fp.read().split(", ")))
        fp.close()
        print("===", self.fileName, "===")
        # print(self.ins)

    def solve1(self):
        print("--- Part One ---")
        facing = 'N'
        x, y = 0, 0
        for instr in self.ins:
            t = instr[0]
            s = int(instr[1::])
            # turn first
            if t == 'L':
                if facing == 'N':
                    facing = 'E'
                elif facing == 'E':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'N'
            else:
                if facing == 'N':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'E'
                elif facing == 'E':
                    facing = 'N'
            # now walk
            if facing == 'N':
                y -= s
            elif facing == 'E':
                x += s
            elif facing == 'S':
                y += s
            elif facing == 'W':
                x -= s
        print("Easter Bunny HQ is", abs(x)+abs(y), "blocks away")

    def solve2(self):
        print("--- Part Two ---")
        facing = 'N'
        x, y = 0, 0
        seen = set()
        seen.add((x, y))
        for instr in self.ins:
            t = instr[0]
            s = int(instr[1::])
            # turn first
            if t == 'L':
                if facing == 'N':
                    facing = 'E'
                elif facing == 'E':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'N'
            else:
                if facing == 'N':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'E'
                elif facing == 'E':
                    facing = 'N'
            # now walk
            while s:
                if facing == 'N':
                    y -= 1
                elif facing == 'E':
                    x += 1
                elif facing == 'S':
                    y += 1
                elif facing == 'W':
                    x -= 1
                s -= 1
                if (x, y) in seen:
                    print("Easter Bunny HQ is", abs(x)+abs(y), "blocks away")
                    return
                seen.add((x, y))


def main():
    Solution.test()
    # Solution.run()

if __name__ == "__main__":
    main()
