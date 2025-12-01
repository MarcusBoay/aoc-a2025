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
        for i in range(0, len(arr)-1):
            line = [arr[i][0], int(arr[i][1::])]
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        # dial starts by pointing at 50
        p = 50
        # total number of times the dial points at 0
        total = 0
        for (i, n) in self.ins:
            if i == "L":
                p -= n
            else:
                p += n
            p %= 100

            if p == 0:
                total += 1

        print(f"Total times the dial points at 0: {total}")



    def solve2(self):
        print("--- Part Two ---")
        # dial starts by pointing at 50
        p = 50
        # total number of times the dial points at 0
        total = 0
        for (i, n) in self.ins:
            if i == "L":
                while n:
                    p -= 1
                    if p == 0:
                        total += 1
                    if p == -1:
                        p = 99
                    n -= 1
            else:
                while n:
                    p += 1
                    if p == 100:
                        p = 0
                        total += 1
                    n -= 1

        print(f"Total times the dial points at 0: {total}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
