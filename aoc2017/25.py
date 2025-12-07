QUIZ_NUMBER = "25"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        row0 = list(map(str, arr[0].split()))
        self.state = row0[0]
        self.check = int(row0[1])
        self.moves = dict()
        for i in range(1, len(arr), 2):
            line1 = arr[i].split()
            line2 = arr[i+1].split()
            self.moves[line1[0]] = [[], []]
            self.moves[line1[0]][0] = [int(line1[2]), int(line1[3]), line1[4]]
            self.moves[line2[0]][1] = [int(line2[2]), int(line2[3]), line2[4]]
        fp.close()
        print("===", self.fileName, "===")
        print(self.moves)

    def solve1(self):
        print("--- Part One ---")
        # t = {"a": True, "b": False, "c": True}
        # ts = sum([t[x] for x in t])
        # print(ts)
        tape = dict()
        i = 0
        for _ in range(self.check):
            if i not in tape:
                tape[i] = 0
            j = tape[i]
            tape[i] = self.moves[self.state][j][0]
            i += self.moves[self.state][j][1]
            self.state = self.moves[self.state][j][2]
        print(f"Diagnositc checksum: {sum([tape[j] for j in tape])}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
