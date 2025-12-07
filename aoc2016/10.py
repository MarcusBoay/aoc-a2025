QUIZ_NUMBER = "10"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve()

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

    def solve(self):
        print("--- Part One ---")
        n = 0
        for instr in self.ins:
            if instr[0] == "value":
                n = max(n, int(instr[5]))
            elif instr[0] == "bot":
                n = max(n, int(instr[6]))
                n = max(n, int(instr[11]))
        bots = [[] for i in range(n+1)]
        outputs = [[] for i in range(n+1)]
        done = [0 for i in range(len(self.ins))]
        while sum(done) < len(self.ins):
            for i in range(len(self.ins)):
                if done[i]:
                    continue
                instr = self.ins[i]
                if instr[0] == "value":
                    bots[int(instr[5])].append(int(instr[1]))
                    done[i] = 1
                elif instr[0] == "bot" and len(bots[int(instr[1])]) == 2:
                    l = bots[int(instr[1])].pop(0)
                    h = bots[int(instr[1])].pop(0)
                    if l > h:
                        l, h = h, l
                    if l == 17 and h == 61:
                        print("Bot number that compares 17 and 61:", int(instr[1]))
                    if instr[5] == "bot":
                        bots[int(instr[6])].append(l)
                    elif instr[5] == "output":
                        outputs[int(instr[6])].append(l)
                    if instr[10] == "bot":
                        bots[int(instr[11])].append(h)
                    if instr[10] == "output":
                        outputs[int(instr[11])].append(h)
                    done[i] = 1
        print("--- Part Two ---")
        print("Result:", outputs[0][0]*outputs[1][0]*outputs[2][0])

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
