QUIZ_NUMBER = "17"

class Solution:
    def run(n, fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(n, fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(25, QUIZ_NUMBER + ".ex.in")

    def __init__(self, n, fileName):
        self.n = n
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = list(map(int, fp.read().split('\n')))
        self.ins.sort()
        fp.close()
        print("===", self.fileName, "===")

    def reset(self):
        self.seen = set()
        self.seenWay = set()
        self.ways = 0

    def solve1(self):
        print("--- Part One ---")
        self.reset()
        self.findMinNumberOfContainers(self.ins)
        print(f"Number of different combinations of containers that can exactly fit all {self.n} liters of eggnog: {self.ways}")


    def findMinNumberOfContainers(self, arr, l=0, seenArr=None, prev=-1):
        if not seenArr:
            seenArr = [False] * len(self.ins)
        self.seen.add(tuple(seenArr))
        if l == self.n and tuple(seenArr) not in self.seenWay:
            self.seenWay.add(tuple(seenArr))
            self.ways += 1
            return
        if l > self.n:
            return

        for i in range(prev+1, len(arr)):
            if not seenArr[i]:
                seenArr[i] = True
                self.findMinNumberOfContainers(arr, l+arr[i], seenArr, i)
                seenArr[i] = False

    def solve2(self):
        print("--- Part Two ---")
        self.reset()
        self.minContainersN = len(self.ins)
        self.minContainers = []
        self.shouldGetMinContainers = False
        self.findMinContainers()
        self.shouldGetMinContainers = True
        self.reset()
        self.findMinContainers()
        self.minWays = []
        for seenArr in self.minContainers:
            curContainers = []
            for i in range(len(seenArr)):
                if seenArr[i]:
                    curContainers.append(self.ins[i])
            self.reset()
            self.findMinNumberOfContainers(curContainers)
            self.minWays.append(self.ways)
        print(f"Number of different combinations with a minimum {self.minContainersN} containers that can exactly fit all {self.n} liters of eggnog: {sum(self.minWays)}")

    def findMinContainers(self, l=0, seenArr=None, prev=-1):
        if not seenArr:
            seenArr = [False] * len(self.ins)
        self.seen.add(tuple(seenArr))
        if l == self.n and tuple(seenArr) not in self.seenWay:
            self.seenWay.add(tuple(seenArr))
            self.ways += 1
            self.minContainersN = min(sum(seenArr), self.minContainersN)
            if self.shouldGetMinContainers and sum(seenArr) == self.minContainersN:
                self.minContainers.append(seenArr[:])
            return
        if l > self.n:
            return

        for i in range(prev+1, len(self.ins)):
            if not seenArr[i]:
                seenArr[i] = True
                self.findMinContainers(l+self.ins[i], seenArr, i)
                seenArr[i] = False

def main():
    Solution.test()
    Solution.run(150)

if __name__ == "__main__":
    main()
