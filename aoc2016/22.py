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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")
        print(self.ins[0:5])

    def solve1(self):
        print("--- Part One ---")
        viablePairs = 0
        for i in range(2, len(self.ins)):
            a = int(self.ins[i][2][0:-1])
            if a == 0:
                continue
            for j in range(2, len(self.ins)):
                if i == j:
                    continue
                b = int(self.ins[j][3][0:-1])
                if a <= b:
                    print(self.ins[i], self.ins[j], a, b)
                    viablePairs += 1
        print(f"Number of viable pairs of nodes: {viablePairs}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
