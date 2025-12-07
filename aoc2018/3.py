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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            self.ins.append(list(map(int, line[::])))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        # find min height and width of fabric
        n, m = 0, 0
        for claim in self.ins:
            m = max(m, claim[2]+claim[4]+1)
            n = max(n, claim[1]+claim[3]+1)
        self.fabric = [['.' for j in range(m)] for i in range(n)]
        # fill fabric with areas
        for claim in self.ins:
            for i in range(claim[2], claim[4]+claim[2]):
                for j in range(claim[1], claim[3]+claim[1]):
                    if self.fabric[i][j] == '.':
                        self.fabric[i][j] = str(claim[0])
                    elif self.fabric[i][j].isdigit():
                        self.fabric[i][j] = 'X'
        # count overlapping areas
        overlapping = 0
        for i in range(m):
            for j in range(n):
                if self.fabric[i][j] == 'X':
                    overlapping += 1
        print("Square inches of overlapping fabric:", overlapping)

    def solve2(self):
        print("--- Part Two ---")
        for claim in self.ins:
            isOverlapping = False
            for i in range(claim[2], claim[4]+claim[2]):
                for j in range(claim[1], claim[3]+claim[1]):
                    if self.fabric[i][j] == 'X':
                        isOverlapping = True
                        break
                if isOverlapping:
                    break
            if not isOverlapping:
                print("Claim ID that doesn't overlap:", claim[0])
                break


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
