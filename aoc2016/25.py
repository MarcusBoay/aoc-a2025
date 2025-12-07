QUIZ_NUMBER = "25"

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
        reg = {"a": 0, "b": 0, "c": 0, "d": 0}

        found = False
        ai = 0
        while not found:
            reg["a"] = ai
            print(f"Checking a = {ai}")
            prevSignal = 1
            i = 0
            while i < len(self.ins):
                inst = self.ins[i]
                # print(i, inst)
                op = inst[0]
                l = inst[1]
                r = None
                if len(inst) > 2:
                    r = inst[2]

                if op == "cpy":
                    if l.isalpha():
                        l = reg[l]
                    else:
                        l = int(l)
                    if isinstance(r, str):
                        reg[r] = l
                elif op == "inc":
                    reg[l] += 1
                elif op == "dec":
                    reg[l] -= 1
                elif op == "jnz":
                    if l.isalpha():
                        l = reg[l]
                    else:
                        l = int(l)
                    if r.isalpha():
                        r = reg[r]
                    else:
                        r = int(r)
                    if l != 0:
                        i -= 1
                        i += r
                elif op == "tgl":
                    if l.isalpha():
                        l = reg[l]
                    else:
                        l = int(l)
                    togI = l+i
                    if togI < len(self.ins):
                        togOp = self.ins[togI][0]
                        if togOp == "dec":
                            self.ins[togI][0] = "inc"
                        elif togOp == "inc":
                            self.ins[togI][0] = "dec"
                        elif togOp == "jnz":
                            self.ins[togI][0] = "cpy"
                        elif togOp == "cpy":
                            self.ins[togI][0] = "jnz"
                        elif togOp == "tgl":
                            self.ins[togI][0] = "inc"
                elif op == "out":
                    if l.isalpha():
                        l = reg[l]
                    else:
                        l = int(l)
                    if prevSignal == l:
                        break
                    prevSignal = l
                i += 1
            ai += 1
        print(f"Value in register 'a': {reg["a"]}")


    def solve2(self):
        print("--- Part Two ---")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
