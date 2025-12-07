QUIZ_NUMBER = "8"

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
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        # symbol table for registers
        # key: value == name: int value
        reg = dict()
        for instr in self.ins:
            LHS = instr[0]
            op = instr[1]
            RHS = int(instr[2])
            condLHS = instr[4]
            condOp = instr[5]
            condRHS = int(instr[6])
            if LHS not in reg:
                reg[LHS] = 0
            if condLHS not in reg:
                reg[condLHS] = 0

            # evaluate condition first
            condition = False
            if condOp == ">" and reg[condLHS] > condRHS:
                condition = True
            elif condOp == ">=" and reg[condLHS]>= condRHS:
                condition = True
            elif condOp == "<" and reg[condLHS] < condRHS:
                condition = True
            elif condOp == "<=" and reg[condLHS] <= condRHS:
                condition = True
            elif condOp == "==" and reg[condLHS] == condRHS:
                condition = True
            elif condOp == "!=" and reg[condLHS] != condRHS:
                condition = True

            if condition:
                if op == "inc":
                    reg[LHS] += RHS
                else:
                    reg[LHS] -= RHS

        regMax = 0
        for r in reg:
            regMax = max(regMax, reg[r])
        print("Largest value in any register after completion:", regMax)

    def solve2(self):
        print("--- Part Two ---")
        # symbol table for registers
        # key: value == name: int value
        reg = dict()
        regMax = 0
        for instr in self.ins:
            LHS = instr[0]
            op = instr[1]
            RHS = int(instr[2])
            condLHS = instr[4]
            condOp = instr[5]
            condRHS = int(instr[6])
            if LHS not in reg:
                reg[LHS] = 0
            if condLHS not in reg:
                reg[condLHS] = 0

            # evaluate condition first
            condition = False
            if condOp == ">" and reg[condLHS] > condRHS:
                condition = True
            elif condOp == ">=" and reg[condLHS]>= condRHS:
                condition = True
            elif condOp == "<" and reg[condLHS] < condRHS:
                condition = True
            elif condOp == "<=" and reg[condLHS] <= condRHS:
                condition = True
            elif condOp == "==" and reg[condLHS] == condRHS:
                condition = True
            elif condOp == "!=" and reg[condLHS] != condRHS:
                condition = True

            if condition:
                if op == "inc":
                    reg[LHS] += RHS
                else:
                    reg[LHS] -= RHS
            regMax = max(regMax, reg[LHS])
        print("Largest value in any register during the process:", regMax)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
