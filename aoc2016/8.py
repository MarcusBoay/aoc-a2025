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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            if line[0] == "rect":
                tmp1 = [line[0]]
                tmp2 = line[1].split('x')
                tmp1.append(tmp2[0])
                tmp1.append(tmp2[1])
                line = tmp1
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        w, h = 50, 6
        # w, h = 8, 4
        screen = [['.' for j in range(w)] for i in range(h)]
        opi = 0
        for op in self.ins:
            opi += 1
            # for row in screen:
            #     print("".join(row))
            # print(opi, op)
            if op[0] == "rect":
                rw, rh = int(op[1]), int(op[2])
                for i in range(rh):
                    for j in range(rw):
                        screen[i][j] = '#'
            elif op[0] == "rotate":
                if op[1] == "row":
                    y = int(op[3])
                    shift = int(op[4])
                    newRow = ['.'] * w
                    for j in range(w):
                        newRow[j] = screen[y][(j-shift)%w]
                    for j in range(w):
                        screen[y][j] = newRow[j]
                elif op[1] == "column":
                    x = int(op[3])
                    shift = int(op[4])
                    newCol = ['.'] * h
                    for i in range(h):
                        newCol[i] = screen[(i-shift)%h][x]
                    for i in range(h):
                        screen[i][x] = newCol[i]

        numberOfLitPixels = 0
        for row in screen:
            numberOfLitPixels += row.count('#')
        print("Number of pixels lit:", numberOfLitPixels)
        for row in screen:
            print("".join(row))

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
