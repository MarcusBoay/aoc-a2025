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
        arr = list(map(int, fp.read().split('\n')))
        self.ins = arr[::]
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        print("Resulting frequency:", sum(self.ins))

    def solve2(self):
        print("--- Part Two ---")
        curFreq = 0
        freq = set()
        freq.add(curFreq)
        fi = 0
        while True:
            curFreq += self.ins[fi%len(self.ins)]
            if curFreq in freq:
                print("First frequency reached twice:", curFreq)
                break
            freq.add(curFreq)
            fi += 1

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
