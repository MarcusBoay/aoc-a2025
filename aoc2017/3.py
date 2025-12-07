QUIZ_NUMBER = "3"

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
        self.ins = int(fp.read())
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        l = 1
        i = 0
        j = 0
        cur = 1
        while cur < self.ins:
            l += 2
            j += 2
            i += 2
            cur += (l*4-4)
        # go back to inner circle
        cur -= (l*4-4)
        i -= 2
        j -= 2
        l -= 2
        # step into the outer circle
        l += 2
        j += 1
        cur += 1
        # expand the coords due to the outer circle
        i += 1
        j += 1

        # run along the length of the outer circle
        cl = l-2
        print(f"currently at {cur}, coords: {i}, {j}, {cl}")
        while cl and cur != self.ins:
            cl -= 1
            i -= 1
            cur += 1
        print(i, j)
        if cur == self.ins:
            self.printSteps(i,j,l)
            return
        cl = l-1
        while cl and cur != self.ins:
            cl -= 1
            j -= 1
            cur += 1
        print(i, j)
        if cur == self.ins:
            self.printSteps(i,j,l)
            return
        cl = l-1
        while cl and cur != self.ins:
            cl -= 1
            i += 1
            cur += 1
        print(i, j)
        if cur == self.ins:
            self.printSteps(i,j,l)
            return
        cl = l-1
        while cl and cur != self.ins:
            cl -= 1
            j += 1
            cur += 1
        print(i, j)
        if cur == self.ins:
            self.printSteps(i,j,l)
            return

    def printSteps(self,i,j,l):
        print(f"d.Number of steps to get to {self.ins}: {self.getSteps(i,j,l)}")

    def getSteps(self,i,j,l):
        i = abs(i - (l//2))
        j = abs(j - (l//2))
        return i+j

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
