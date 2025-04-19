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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            self.ins.append(line[:])
            # newLine = []
            # for col in line:
            #     if col.isdigit():
            #         newLine.append(int(col))
            #     else:
            #         newLine.append(col)
            # self.ins.append(newLine[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        self.symbolTable = dict()
        self.lastSoundPlayed = None # [register name, sound frequency]

        i = 0
        while i < len(self.ins):
            instr = self.ins[i]
            if len(instr) > 1 and instr[1] not in self.symbolTable:
                self.symbolTable[instr[1]] = 0
            if len(instr) > 2 and instr[2].isalpha() and instr[2] not in self.symbolTable:
                self.symbolTable[instr[2]] = 0
            if instr[0] == "snd":
                self.lastSoundPlayed = [instr[1], self.symbolTable[instr[1]]]
            elif instr[0] == "set":
                if instr[2].isalpha():
                    self.symbolTable[instr[1]] = int(self.symbolTable[instr[2]])
                else:
                    self.symbolTable[instr[1]] = int(instr[2])
            elif instr[0] == "add":
                if instr[2].isalpha():
                    self.symbolTable[instr[1]] += int(self.symbolTable[instr[2]])
                else:
                    self.symbolTable[instr[1]] += int(instr[2])
            elif instr[0] == "mul":
                if instr[2].isalpha():
                    self.symbolTable[instr[1]] *= int(self.symbolTable[instr[2]])
                else:
                    self.symbolTable[instr[1]] *= int(instr[2])
            elif instr[0] == "mod":
                if instr[2].isalpha():
                    self.symbolTable[instr[1]] %= int(self.symbolTable[instr[2]])
                else:
                    self.symbolTable[instr[1]] %= int(instr[2])
            elif instr[0] == "rcv":
                if self.symbolTable[instr[1]] > 0:
                    print(f"Value of first recovered frequency: {self.lastSoundPlayed}")
                    return
            elif instr[0] == "jgz":
                if self.symbolTable[instr[1]] > 0:
                    i -= 1
                    if instr[2].isalpha():
                        i += self.symbolTable[instr[2]]
                    else:
                        i += int(instr[2])
                    pass
            i += 1

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
