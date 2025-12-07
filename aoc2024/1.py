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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = list(map(int, arr[i].split()))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        l, r = [], []
        for row in self.ins:
            l.append(row[0])
            r.append(row[1])
        l.sort()
        r.sort()
        totalDist = 0
        for i in range(len(l)):
            totalDist += abs(l[i] - r[i])
        print("Total distance between lists:", totalDist)

    def solve2(self):
        print("--- Part Two ---")
        l, r = [], []
        for row in self.ins:
            l.append(row[0])
            r.append(row[1])
        similarityScore = 0
        rCount = dict()
        for x in r:
            if x not in rCount:
                rCount[x] = 0
            rCount[x] += 1
        for x in l:
            if x in rCount:
                similarityScore += x * rCount[x]
        print("Similarity score:", similarityScore)


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
