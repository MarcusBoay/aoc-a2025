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
        pos = dict() # ((i,j), 0(clean), 1(weakened), 2(infected), 3(flagged))
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                pos[(i,j)] = 0
                if self.ins[i][j] == '#':
                    pos[(i,j)] = 2

        i, j = len(self.ins)//2, len(self.ins[0])//2
        facing = 0 # 0(U), (1)R, (2)D, (3)L
        N = 10000000
        numberOfInfectedBursts = 0
        for n in range(N):
            # turn
            if pos[(i,j)] == 0: # clean, turn left
                facing = (facing - 1) % 4
            elif pos[(i,j)] == 1: # weakened, face the same direction
                facing = facing
            elif pos[(i,j)] == 2: # infected, turn right
                facing = (facing + 1) % 4
            elif pos[(i,j)] == 3: # flagged, reverse direction
                facing = (facing + 2) % 4

            # clean/weaken/infect/flag
            pos[(i,j)] = (pos[(i,j)] + 1) % 4
            if pos[(i,j)] == 2:
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
                pos[(i,j)] = 0

        print(f"Number of bursts that cause a node to become infected: {numberOfInfectedBursts}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
