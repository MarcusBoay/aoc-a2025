QUIZ_NUMBER = "15"

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
            line = list(map(int, arr[i].split()))
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        d = -1
        didFallThrough = False
        while not didFallThrough:
            d += 1
            didFallThrough = True
            for i in range(len(self.ins)):
                discI = self.ins[i][0]
                discPosI = self.ins[i][3]
                discPosN = self.ins[i][1]
                if ((discPosI + discI + d)%discPosN != 0):
                    didFallThrough = False
                    break
        print(f"First time we can press the button to get a capsule: {d}")

    def solve2(self):
        print("--- Part Two ---")
        d = -1
        didFallThrough = False
        self.ins.append([len(self.ins)+1, 11, 0, 0])
        while not didFallThrough:
            d += 1
            didFallThrough = True
            for i in range(len(self.ins)):
                discI = self.ins[i][0]
                discPosI = self.ins[i][3]
                discPosN = self.ins[i][1]
                if ((discPosI + discI + d)%discPosN != 0):
                    didFallThrough = False
                    break
        print(f"First time we can press the button to get a capsule: {d}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
