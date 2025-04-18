QUIZ_NUMBER = "20"

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
        l, r = 0, self.ins
        hn = 0
        m = 0
        while l < r:
            m = (l+r)//2
            hn = 0
            for i in range(1, m+1):
                if not m % i:
                    hn += i
            if hn > self.ins//10:
                r = m
            else:
                l = m + 1
        print(l, r, hn, m)

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
