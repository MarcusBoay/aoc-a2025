QUIZ_NUMBER = "23"

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
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        reg = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
        }

        i = 0
        numberOfTimesMulInvoked = 0
        while i < len(self.ins):
            op = self.ins[i][0]
            l = self.ins[i][1]
            r = self.ins[i][2]
            r = reg[r] if r.isalpha() else int(r)

            if op == "set":
                reg[l] = r
            elif op == "sub":
                reg[l] -= r
            elif op == "mul":
                reg[l] *= r
                numberOfTimesMulInvoked += 1
            elif op == "jnz":
                l = reg[l] if l.isalpha() else int(l)
                if l != 0:
                    i -= 1
                    i += r

            i += 1

        print(f"Number of times 'mul' instruction is invoked: {numberOfTimesMulInvoked}")


    def solve2(self):
        print("--- Part Two ---")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
