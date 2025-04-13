QUIZ_NUMBER = "6"
import copy

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
        for line in arr:
            line = list(map(str, line))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")
        # find start pos
        si, sj = -1, -1
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                if self.ins[i][j] == '^':
                    si, sj = i, j
                    break
            if si != -1:
                break
        self.si, self.sj = si, sj


    def solve1(self):
        print("--- Part One ---")
        si, sj = self.si, self.sj
        facing = 0 # 0 = up, 1 = right, 2 = down, 3 = left
        maze = copy.deepcopy(self.ins)

        uniquePaths = 0
        while (0 <= si < len(maze)) and \
              (0 <= sj < len(maze[0])):
            if maze[si][sj] != 'X':
                maze[si][sj] = 'X'
                uniquePaths += 1
            if facing == 0:
                if (si > 0 and maze[si-1][sj] in ".X") or \
                    si == 0:
                    si -= 1
                else:
                    facing += 1
            elif facing == 1:
                if (sj < len(maze[si])-1 and maze[si][sj+1] in ".X") or \
                    sj == len(maze[si])-1:
                    sj += 1
                else:
                    facing += 1
            elif facing == 2:
                if (si < len(maze)-1 and maze[si+1][sj] in ".X") or \
                    si == len(maze)-1:
                    si += 1
                else:
                    facing += 1
            elif facing == 3:
                if (sj > 0 and maze[si][sj-1] in ".X") or \
                    sj == 0:
                    sj -= 1
                else:
                    facing = 0
        print("Number of distinct position visited:", uniquePaths)


    def solve2(self):
        print("--- Part Two ---")
        # try to obstruct every position
        numberOfObstructions = 0
        for oi in range(len(self.ins)):
            for oj in range(len(self.ins[oi])):
                # print(oi, oj)
                si, sj = self.si, self.sj
                facing = 0 # 0 = up, 1 = right, 2 = down, 3 = left
                maze = copy.deepcopy(self.ins)
                if maze[oi][oj] == '.':
                    maze[oi][oj] = 'O'
                    uniquePaths = 0
                    while (0 <= si < len(maze)) and \
                        (0 <= sj < len(maze[0])):
                        if maze[si][sj] != 'X':
                            maze[si][sj] = 'X'
                            uniquePaths += 1
                        if facing == 0:
                            if (si > 0 and maze[si-1][sj] in ".X") or \
                                si == 0:
                                si -= 1
                            else:
                                facing += 1
                        elif facing == 1:
                            if (sj < len(maze[si])-1 and maze[si][sj+1] in ".X") or \
                                sj == len(maze[si])-1:
                                sj += 1
                            else:
                                facing += 1
                        elif facing == 2:
                            if (si < len(maze)-1 and maze[si+1][sj] in ".X") or \
                                si == len(maze)-1:
                                si += 1
                            else:
                                facing += 1
                        elif facing == 3:
                            if (sj > 0 and maze[si][sj-1] in ".X") or \
                                sj == 0:
                                sj -= 1
                            else:
                                facing = 0
                                if uniquePaths == 0:
                                    numberOfObstructions += 1
                                    # for row in maze:
                                    #     print("".join(row))
                                    # print()
                                    break
                                uniquePaths = 0
        print("Number of different positions for the obstruction:", numberOfObstructions)



def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
