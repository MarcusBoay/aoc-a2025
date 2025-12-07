QUIZ_NUMBER = "13"
# FIXME: Both function never run to completion...
class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        # solution.solve1()
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

    def solve1(self):
        print("--- Part One ---")
        nameMap = dict()
        n = 0
        for line in self.ins:
            if line[0] not in nameMap:
                nameMap[line[0]] = n
                n += 1
        self.happinessMap = [[0 for y in range(n)] for x in range(n)]
        for line in self.ins:
            nameI = nameMap[line[0]]
            nameJ = nameMap[line[10]]
            self.happinessMap[nameI][nameJ] = int(line[3])
            self.happinessMap[nameI][nameJ] *= -1 if line[2] == "lose" else 1
        # for i in range(n):
        #     sitting[i] = i

        self.maxHappy = 0
        self.n = n
        def backtrack():
            n = self.n
            if len(self.sat) == n:
                curHappy = 0
                for k in range(n):
                    si, sj = self.sitting[k], self.sitting[(k+1)%n]
                    curHappy += self.happinessMap[si][sj] + self.happinessMap[sj][si]
                # print(curHappy)
                self.maxHappy = max(self.maxHappy, curHappy)
                print(self.maxHappy)
                return

            for i in range(n):
                if i not in self.sat:
                    for j in range(n):
                        if self.sitting[j] == -1:
                            self.sitting[j] = i
                            self.sat.add(i)
                            backtrack()
                            self.sat.remove(i)
                            self.sitting[j] = -1
        self.sitting = [-1] * n
        self.sat = set()
        backtrack()
        print("evrybdy hapi :)", self.maxHappy)


    def solve2(self):
        print("--- Part Two ---")
        nameMap = dict()
        n = 0
        for line in self.ins:
            if line[0] not in nameMap:
                nameMap[line[0]] = n
                n += 1
        nameMap["me"] = n
        n += 1
        self.happinessMap = [[0 for y in range(n)] for x in range(n)]
        for line in self.ins:
            nameI = nameMap[line[0]]
            nameJ = nameMap[line[10]]
            self.happinessMap[nameI][nameJ] = int(line[3])
            self.happinessMap[nameI][nameJ] *= -1 if line[2] == "lose" else 1
        # for i in range(n):
        #     sitting[i] = i

        self.maxHappy = 0
        self.n = n
        def backtrack():
            n = self.n
            if len(self.sat) == n:
                curHappy = 0
                for k in range(n):
                    si, sj = self.sitting[k], self.sitting[(k+1)%n]
                    curHappy += self.happinessMap[si][sj] + self.happinessMap[sj][si]
                if curHappy > self.maxHappy:
                    self.maxHappy = max(self.maxHappy, curHappy)
                    print(curHappy)
                return

            for i in range(n):
                if i not in self.sat:
                    for j in range(n):
                        if self.sitting[j] == -1:
                            self.sitting[j] = i
                            self.sat.add(i)
                            backtrack()
                            self.sat.remove(i)
                            self.sitting[j] = -1
        self.sitting = [-1] * n
        self.sat = set()
        backtrack()
        print("evrybdy hapi :)", self.maxHappy)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
