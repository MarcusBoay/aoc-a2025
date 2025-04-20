QUIZ_NUMBER = "20"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.p = []
        self.v = []
        self.a = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = list(map(int, arr[i].split(",")))
            self.p.append(line[0:3])
            self.v.append(line[3:6])
            self.a.append(line[6:9])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        minD = 999999999999
        minI = 0
        # s = ut + 0.5at^2
        t = 1000
        for i in range(len(self.p)):
            sx = self.v[i][0]*t + 0.5*self.a[i][0]*t*t
            sy = self.v[i][1]*t + 0.5*self.a[i][1]*t*t
            sz = self.v[i][2]*t + 0.5*self.a[i][2]*t*t
            sx += self.p[i][0]
            sy += self.p[i][1]
            sz += self.p[i][2]
            absS = abs(sx) + abs(sy) + abs(sz)
            if absS < minD:
                minD = absS
                minI = i
        print(f"Particle that will stay the closest to origin: {minI}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
