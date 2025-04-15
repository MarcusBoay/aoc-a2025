QUIZ_NUMBER = "4"
import hashlib

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
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        i = 0
        while True:
            t = self.ins + str(i)
            m = hashlib.md5()
            m.update(t.encode())
            h = m.hexdigest()
            if h[0:5] == "00000":
                print("Answer:", i)
                return
            i += 1

    def solve2(self):
        print("--- Part Two ---")
        i = 0
        while True:
            t = self.ins + str(i)
            m = hashlib.md5()
            m.update(t.encode())
            h = m.hexdigest()
            if h[0:6] == "000000":
                print("Answer:", i)
                return
            i += 1

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
