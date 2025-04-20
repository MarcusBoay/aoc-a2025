QUIZ_NUMBER = "22"

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
        pos = dict() # ((i,j), infected=true/false)
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                pos[(i,j)] = False
                if self.ins[i][j] == '#':
                    pos[(i,j)] = True

        i, j = len(self.ins)//2, len(self.ins[0])//2
        facing = 0 # 0(U), (1)R, (2)D, (3)L
        N = 10000
        numberOfInfectedBursts = 0
        for n in range(N):
            # turn right/left
            if pos[(i,j)]:
                facing = (facing + 1) % 4
            else:
                facing = (facing - 1) % 4

            # infect/clean
            pos[(i,j)] = not pos[(i,j)]
            if pos[(i,j)]:
                numberOfInfectedBursts += 1

            # move forward
            if facing == 0:
                i -= 1
            elif facing == 1:
                j += 1
            elif facing == 2:
                i += 1
            elif facing == 3:
                j -= 1

            # add pos if new
            if (i,j) not in pos:
                pos[(i,j)] = False

        print(f"Number of bursts that cause a node to become infected: {numberOfInfectedBursts}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
