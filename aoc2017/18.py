import asyncio
import threading
from time import sleep
from multiprocessing import Process, Lock
import queue

QUIZ_NUMBER = "18"

mutex = Lock()
q0 = queue.Queue()
q1 = queue.Queue()

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
        symbolTable = dict()
        lastSoundPlayed = None # [register name, sound frequency]

        i = 0
        while i < len(self.ins):
            instr = self.ins[i]
            if len(instr) > 1 and instr[1] not in symbolTable:
                symbolTable[instr[1]] = 0
            if len(instr) > 2 and instr[2].isalpha() and instr[2] not in symbolTable:
                symbolTable[instr[2]] = 0
            if instr[0] == "snd":
                lastSoundPlayed = [instr[1], symbolTable[instr[1]]]
            elif instr[0] == "set":
                if instr[2].isalpha():
                    symbolTable[instr[1]] = int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] = int(instr[2])
            elif instr[0] == "add":
                if instr[2].isalpha():
                    symbolTable[instr[1]] += int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] += int(instr[2])
            elif instr[0] == "mul":
                if instr[2].isalpha():
                    symbolTable[instr[1]] *= int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] *= int(instr[2])
            elif instr[0] == "mod":
                if instr[2].isalpha():
                    symbolTable[instr[1]] %= int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] %= int(instr[2])
            elif instr[0] == "rcv":
                if symbolTable[instr[1]] > 0:
                    print(f"Value of first recovered frequency: {lastSoundPlayed}")
                    return
            elif instr[0] == "jgz":
                if symbolTable[instr[1]] > 0:
                    i -= 1
                    if instr[2].isalpha():
                        i += symbolTable[instr[2]]
                    else:
                        i += int(instr[2])
                    pass
            i += 1

    def _solve2(self, pi):
        i = 0
        symbolTable = dict()
        symbolTable["p"] = pi
        # ti = 0
        while i < len(self.ins):
            # ti += 1
            # if ti % 10000 == 0:
            #     print(pi, symbolTable)
            instr = self.ins[i]
            if len(instr) > 1 and instr[1].isalpha() and instr[1] not in symbolTable:
                symbolTable[instr[1]] = 0
            if len(instr) > 2 and instr[2].isalpha() and instr[2] not in symbolTable:
                symbolTable[instr[2]] = 0
            if instr[0] == "snd":
                self.sndCount[pi] += 1
                val = 0
                if instr[1].isalpha():
                    val = int(symbolTable[instr[1]])
                else:
                    val = int(instr[1])
                if pi == 0:
                    q1.put(val)
                else:
                    q0.put(val)
            elif instr[0] == "set":
                if instr[2].isalpha():
                    symbolTable[instr[1]] = int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] = int(instr[2])
            elif instr[0] == "add":
                if instr[2].isalpha():
                    symbolTable[instr[1]] += int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] += int(instr[2])
            elif instr[0] == "mul":
                if instr[2].isalpha():
                    symbolTable[instr[1]] *= int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] *= int(instr[2])
            elif instr[0] == "mod":
                if instr[2].isalpha():
                    symbolTable[instr[1]] %= int(symbolTable[instr[2]])
                else:
                    symbolTable[instr[1]] %= int(instr[2])
            elif instr[0] == "rcv":
                if (pi == 0 and q0.empty()) or \
                   (pi == 1 and q1.empty()):
                    # print(pi, "waiting...")
                    self.isWaiting[pi] = True
                    i -= 1
                else:
                    self.isWaiting[pi] = False
                    if pi == 0:
                        symbolTable[instr[1]] = q0.get(0)
                    else:
                        symbolTable[instr[1]] = q1.get(0)
            elif instr[0] == "jgz":
                cond = symbolTable[instr[1]] if instr[1].isalpha() else int(instr[1])
                if cond > 0:
                    i -= 1
                    if instr[2].isalpha():
                        i += symbolTable[instr[2]]
                    else:
                        i += int(instr[2])
            i += 1

    def solve2(self):
        print("--- Part Two ---")
        self.symbolTable = [dict(), dict()]
        # lastSoundPlayed = [None, None] # [register name, sound frequency]
        # self.q =
        self.sndCount = [0, 0]
        self.isWaiting = [False, False]
        t0 = threading.Thread(target=self._solve2, args=(0, ))
        t1 = threading.Thread(target=self._solve2, args=(1, ))
        t0.start()
        t1.start()
        while True:
            try:
                sleep(1)
                # if self.isWaiting[0] and self.isWaiting[1]:
                print(f"Number of times programs sent values: {self.sndCount}")
                    # break
            except:
                break
        t0.join()
        t1.join()
        print(f"Number of times programs sent values: {self.sndCount}")


def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
