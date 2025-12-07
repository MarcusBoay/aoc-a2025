QUIZ_NUMBER = "7"

class Solution:
    def run(fileName):
        solution = Solution(fileName)
        for i in range(1000): # brute force...
            solution.solve()
        print("Signal provided to wire 'a':", solution.symbolTable["a"])

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.symbolTable = dict()
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve(self):
        for instr in self.ins:
            # 123 -> x
            if len(instr) == 2:
                self.opAssign(instr)
            # NOT x -> h
            elif len(instr) == 3 and instr[0] == "NOT":
                self.opNot(instr)
            # x AND y -> d
            elif len(instr) == 4 and instr[1] == "AND":
                self.opAnd(instr)
            # x OR y -> e
            elif len(instr) == 4 and instr[1] == "OR":
                self.opOr(instr)
            # x LSHIFT 2 -> f
            # x RSHIFT 2 -> g
            elif len(instr) == 4 and \
                 (instr[1] == "LSHIFT" or instr[1] == "RSHIFT"):
                self.opShift(instr)

        # for k in sorted(self.symbolTable):
        #     print(k, self.symbolTable[k])

    def initSym(self, sym):
        """
        Initializes sym in self.symbolTable with 0.
        """
        if not sym.isdigit() and sym not in self.symbolTable:
            self.symbolTable[sym] = 0

    def opAssign(self, instr):
        """
        The format of instr is "y x" (y can be a literal int).
        """
        LHS = instr[0]
        RHS = instr[1]
        self.initSym(LHS)
        self.initSym(RHS)
        if LHS.isdigit():
            self.symbolTable[RHS] = int(LHS)
        else:
            self.symbolTable[RHS] = self.symbolTable[LHS]

    def opNot(self, instr):
        """
        The format of instr is "NOT y x" (y can be a literal int).
        """
        LHS = instr[1]
        RHS = instr[2]
        self.initSym(LHS)
        self.initSym(RHS)
        if LHS.isdigit():
            self.symbolTable[RHS] = 0xFFFF & (~int(LHS))
        else:
            self.symbolTable[RHS] = 0xFFFF & (~self.symbolTable[LHS])

    def opAnd(self, instr):
        """
        The format of instr is "x AND y d" (x/y can be a literal int).
        """
        LHS = instr[0]
        RHS = instr[2]
        result = instr[3]
        self.initSym(LHS)
        self.initSym(RHS)
        self.initSym(result)
        if LHS.isdigit():
            LHS = int(LHS)
        else:
            LHS = self.symbolTable[LHS]
        if RHS.isdigit():
            RHS = int(RHS)
        else:
            RHS = self.symbolTable[RHS]
        self.symbolTable[result] = LHS & RHS

    def opOr(self, instr):
        """
        The format of instr is "x OR y d" (x/y can be a literal int). (? todo)
        """
        LHS = instr[0]
        RHS = instr[2]
        result = instr[3]
        self.initSym(LHS)
        self.initSym(RHS)
        self.initSym(result)
        if LHS.isdigit():
            LHS = int(LHS)
        else:
            LHS = self.symbolTable[LHS]
        if RHS.isdigit():
            RHS = int(RHS)
        else:
            RHS = self.symbolTable[RHS]
        self.symbolTable[result] = LHS | RHS

    def opShift(self, instr):
        """
        The format of instr is "x (LSHIFT|RSHIFT) 2 d".
        """
        LHS = instr[0]
        op = instr[1]
        RHS = instr[2]
        result = instr[3]
        self.initSym(LHS)
        self.initSym(result)
        if op == "LSHIFT":
            self.symbolTable[result] = self.symbolTable[LHS] << int(RHS)
        elif op == "RSHIFT":
            self.symbolTable[result] =  self.symbolTable[LHS] >> int(RHS)


def main():
    # Solution.test()
    print("--- Part One ---")
    Solution.run(QUIZ_NUMBER + ".in")
    print("--- Part Two ---")
    Solution.run(QUIZ_NUMBER + ".2.in")

if __name__ == "__main__":
    main()
