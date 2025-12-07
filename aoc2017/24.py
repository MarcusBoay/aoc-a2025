QUIZ_NUMBER = "24"

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
            line = list(map(int, arr[i].split('/')))
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        self.seen = set()
        self.maxStrength = 0
        def getStrength(next, strength):
            isEnd = True
            for c in self.ins:
                for i in range(len(c)):
                    ce = c[i]
                    ce2 = c[(i+1)%len(c)]
                    if tuple(c) not in self.seen and ce == next:
                        isEnd = False
                        self.seen.add(tuple(c))
                        getStrength(ce2, strength+ce+ce2)
                        self.seen.remove(tuple(c))

            if isEnd and strength > self.maxStrength:
                self.maxStrength = max(strength, self.maxStrength)
        getStrength(0, 0)
        print(f"Strength of the strongest bridge: {self.maxStrength}")



    def solve2(self):
        print("--- Part Two ---")
        self.seen = set()
        self.maxStrength = 0
        self.maxLength = 0
        def getLongestStrength(next, strength):
            isEnd = True
            for c in self.ins:
                for i in range(len(c)):
                    ce = c[i]
                    ce2 = c[(i+1)%len(c)]
                    if tuple(c) not in self.seen and ce == next:
                        isEnd = False
                        self.seen.add(tuple(c))
                        getLongestStrength(ce2, strength+ce+ce2)
                        self.seen.remove(tuple(c))

            if isEnd and len(self.seen) >= self.maxLength:
                if len(self.seen) == self.maxLength:
                    self.maxStrength = max(strength, self.maxStrength)
                else:
                    self.maxStrength = strength
                self.maxLength = len(self.seen)
        getLongestStrength(0, 0)
        print(f"Strength of the longest bridge ({self.maxLength}): {self.maxStrength}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
