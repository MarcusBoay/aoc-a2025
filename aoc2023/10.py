QUIZ_NUMBER = "10"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.seen = set()
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = list(arr[i])
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")

        # get starting position
        si, sj = -1, -1
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                if self.ins[i][j] == 'S':
                    si, sj = i, j
                    break
            if si != -1:
                break

        paths = [[si, sj]]
        step = 0
        while paths:
            nextPaths = []
            step += 1
            while paths:
                cur = paths.pop(0)
                self.seen.add((cur[0], cur[1]))
                # up
                if cur[0]-1 >= 0 and \
                   (cur[0]-1, cur[1]) not in self.seen and \
                   self.ins[cur[0]][cur[1]] in "S|JL" and \
                   self.ins[cur[0]-1][cur[1]] in "|F7":
                    nextPaths.append([cur[0]-1, cur[1]])
                    self.seen.add((cur[0]-1, cur[1]))
                # down
                if cur[0]+1 < len(self.ins) and \
                   (cur[0]+1, cur[1]) not in self.seen and \
                   self.ins[cur[0]][cur[1]] in "S|F7" and \
                   self.ins[cur[0]+1][cur[1]] in "|JL":
                    nextPaths.append([cur[0]+1, cur[1]])
                    self.seen.add((cur[0]+1, cur[1]))
                # left
                if cur[1]-1 >= 0 and \
                   (cur[0], cur[1]-1) not in self.seen and \
                   self.ins[cur[0]][cur[1]] in "S-7J" and \
                   self.ins[cur[0]][cur[1]-1] in "-FL":
                    nextPaths.append([cur[0], cur[1]-1])
                    self.seen.add((cur[0], cur[1]-1))
                # right
                if cur[1]+1 < len(self.ins) and \
                   (cur[0], cur[1]+1) not in self.seen and \
                   self.ins[cur[0]][cur[1]] in "S-FL" and \
                   self.ins[cur[0]][cur[1]+1] in "-7J":
                    nextPaths.append([cur[0], cur[1]+1])
                    self.seen.add((cur[0], cur[1]+1))
                # for next in nextPaths:
                #     self.ins[next[0]][next[1]] = step
            paths = nextPaths[::]
        print("Farthest step from the starting position:", step-1)


    def solve2(self):
        print("--- Part Two ---")
        # part two depends on part one

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
