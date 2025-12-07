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
        self.ins2 = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)-1):
            line = None
            if i == len(arr)-2:
                line = list(map(str, arr[i].strip().split()))
            else:
                line = list(map(int, arr[i].strip().split()))
            line2 = arr[i].split()
            self.ins.append(line[::])
        self.ins2 = arr[::]
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total = 0
        for j in range(len(self.ins[0])):
            cur = 0
            op = self.ins[len(self.ins)-1][j]
            for i in range(len(self.ins)-1):
                if op == '+':
                    cur += self.ins[i][j]
                elif op == '-':
                    cur -= self.ins[i][j]
                elif op == '*':
                    if cur == 0:
                        cur = 1
                    cur *= self.ins[i][j]
            total += cur
        print(f"Grand total:\n{total}")


    def solve2(self):
        print("--- Part Two ---")
        total = 0
        j2 = 0
        for j in range(len(self.ins[0])):
            op = self.ins[len(self.ins)-1][j]
            col = []
            while j2 < len(self.ins2[0]):
                cur = 0
                did_find_digit = False
                for i in range(len(self.ins2)-2):
                    if self.ins2[i][j2] != ' ':
                        did_find_digit = True
                        cur *= 10
                        cur += int(self.ins2[i][j2])
                if cur > 0:
                    col.append(cur)
                j2 += 1
                if not did_find_digit:
                    break
            cur = 0
            for num in col:
                if op == '+':
                    cur += num
                elif op == '*':
                    if cur == 0:
                        cur = 1
                    cur *= num
            total += cur
        print(f"Grand total:\n{total}")


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
