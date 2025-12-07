QUIZ_NUMBER = "6"

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
        self.ins = list(map(int, fp.read().split()))
        fp.close()
        print("===", self.fileName, "===")
        # print(self.ins)

    def solve1(self):
        print("--- Part One ---")
        seen = set()
        banks = self.ins[::]
        n = len(banks)
        timesRedistributed = 0
        while tuple(banks) not in seen:
            # add to seen
            seen.add(tuple(banks))

            # find max
            mi = 0
            maxBank = 0
            for i in range(n):
                if maxBank < banks[i]:
                    mi = i
                    maxBank = banks[i]

            # redistribute
            banks[mi] = 0
            while maxBank:
                mi += 1
                mi %= n
                banks[mi] += 1
                maxBank -= 1
            timesRedistributed += 1
        print("Times redistributed:", timesRedistributed)
        self.ins = banks[::]

    def solve2(self):
        print("--- Part Two ---")
        timesRedistributed = 0
        banks = self.ins[::]
        seen = set()
        n = len(banks)
        while tuple(banks) not in seen:
            # add to seen
            seen.add(tuple(banks))

            # find max
            mi = 0
            maxBank = 0
            for i in range(n):
                if maxBank < banks[i]:
                    mi = i
                    maxBank = banks[i]

            # redistribute
            banks[mi] = 0
            while maxBank:
                mi += 1
                mi %= n
                banks[mi] += 1
                maxBank -= 1
            timesRedistributed += 1
        print("Loop size:", timesRedistributed)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
