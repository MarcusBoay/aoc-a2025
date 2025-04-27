QUIZ_NUMBER = "21"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in", pwd="abcdefgh"):
        solution = Solution(fileName, pwd)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in", "abcdefgh")

    def __init__(self, fileName, pwd):
        self.ins = []
        self.password = pwd
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
        pwd = list(map(str, self.password))
        for inst in self.ins:
            print(f"{"".join(pwd)} - {" ".join(inst)}")
            if inst[0] == "swap":
                if inst[1] == "position":
                    i, j = int(inst[2]), int(inst[5])
                    pwd[i], pwd[j] = pwd[j], pwd[i]
                elif inst[1] == "letter":
                    li, lj = inst[2], inst[5]
                    i, j = 0, 0
                    for k in range(len(pwd)):
                        if pwd[k] == li:
                            i = k
                        if pwd[k] == lj:
                            j = k
                    pwd[i], pwd[j] = pwd[j], pwd[i]
            elif inst[0] == "rotate":
                if inst[1] == "based":
                    l = inst[6]
                    i = 0
                    for j in range(len(pwd)):
                        if pwd[j] == l:
                            i = j
                            break
                    r = 1 + i
                    if i >= 4:
                        r += 1
                    pwd = pwd[len(pwd)-r:] + pwd[0:len(pwd)-r]
                else: # left/right
                    r = int(inst[2])
                    if inst[1] == "left":
                        pwd = pwd[r:] + pwd[0:r]
                    elif inst[1] == "right":
                        pwd = pwd[len(pwd)-r:] + pwd[0:len(pwd)-r]
            elif inst[0] == "reverse":
                i, j = int(inst[2]), int(inst[4])
                while i < j:
                    pwd[i], pwd[j] = pwd[j], pwd[i]
                    i += 1
                    j -= 1
            elif inst[0] == "move":
                i, j = int(inst[2]), int(inst[5])
                c = pwd.pop(i)
                pwd.insert(j, c)
        print(f"The result of scrambling '{self.password}': {"".join(pwd)}")

    def solve2(self):
        print("--- Part Two ---")
        # scrambledPwd = "decab" if self.fileName == QUIZ_NUMBER + ".ex.in" else "fbgdceah"
        scrambledPwd = "abcdefgh" if self.fileName == QUIZ_NUMBER + ".ex.in" else "fbgdceah"
        pwd = list(scrambledPwd)
        for instI in range(len(self.ins)-1, -1, -1):
            inst = self.ins[instI]
            print(f"{"".join(pwd)} - {" ".join(inst)}")
            if inst[0] == "swap":
                if inst[1] == "position":
                    i, j = int(inst[2]), int(inst[5])
                    pwd[i], pwd[j] = pwd[j], pwd[i]
                elif inst[1] == "letter":
                    li, lj = inst[2], inst[5]
                    i, j = 0, 0
                    for k in range(len(pwd)):
                        if pwd[k] == li:
                            i = k
                        if pwd[k] == lj:
                            j = k
                    pwd[i], pwd[j] = pwd[j], pwd[i]
            elif inst[0] == "rotate":
                if inst[1] == "based":
                    l = inst[6]
                    j = 0
                    for k in range(len(pwd)):
                        if pwd[k] == l:
                            j = k
                            break
                    r = 999
                    rotate = [9,1,6,2,7,3,8,4]
                    r = rotate[j]
                    pwd = pwd[r%len(pwd):] + pwd[:r%len(pwd)]
                else: # left/right
                    r = int(inst[2])
                    if inst[1] == "left":
                        pwd = pwd[len(pwd)-r:] + pwd[0:len(pwd)-r]
                    elif inst[1] == "right":
                        pwd = pwd[r:] + pwd[0:r]
            elif inst[0] == "reverse":
                i, j = int(inst[2]), int(inst[4])
                while i < j:
                    pwd[i], pwd[j] = pwd[j], pwd[i]
                    i += 1
                    j -= 1
            elif inst[0] == "move":
                i, j = int(inst[2]), int(inst[5])
                c = pwd.pop(j)
                pwd.insert(i, c)
        print(f"The result of un-scrambling '{scrambledPwd}': {"".join(pwd)}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
