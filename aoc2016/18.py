QUIZ_NUMBER = "18"

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
        self.ins = list(map(str, fp.read()))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        room = [self.ins[:]]
        n = 40
        # uncover every row in the room
        for i in range(n-1):
            nextRow = []
            for j in range(len(room[i])):
                l = room[i][j-1] if j-1 >= 0 else '.'
                c = room[i][j]
                r = room[i][j+1] if j+1 < len(room[i]) else '.'
                if (l == '^' and c == '^' and r == '.') or \
                   (l == '.' and c == '^' and r == '^') or \
                   (l == '^' and c == '.' and r == '.') or \
                   (l == '.' and c == '.' and r == '^'):
                    nextRow.append('^')
                else:
                    nextRow.append('.')
            room.append(nextRow[:])

        # get number of safe tiles
        safeTiles = 0
        for i in range(len(room)):
            for t in room[i]:
                if t == '.':
                    safeTiles += 1
        print(f"Number of safe tiles: {safeTiles}")
        # for row in room:
        #     print("".join(row))


    def solve2(self):
        print("--- Part Two ---")
        row = self.ins[:]
        n = 400000
        safeTiles = 0
        for t in row:
            if t == '.':
                safeTiles += 1

        # uncover next row in room and get running sum of safe tiles
        for i in range(n-1):
            nextRow = []
            for j in range(len(row)):
                l = row[j-1] if j-1 >= 0 else '.'
                c = row[j]
                r = row[j+1] if j+1 < len(row) else '.'
                if (l == '^' and c == '^' and r == '.') or \
                   (l == '.' and c == '^' and r == '^') or \
                   (l == '^' and c == '.' and r == '.') or \
                   (l == '.' and c == '.' and r == '^'):
                    nextRow.append('^')
                else:
                    nextRow.append('.')
                    safeTiles += 1
            row = nextRow[:]
        print(f"Number of safe tiles: {safeTiles}")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
