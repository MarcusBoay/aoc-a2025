QUIZ_NUMBER = "16"

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
        # l = 20
        l = 272

        # generate data
        a = self.ins[:]
        while len(a) < l:
            b = list(map(str, a))
            b.reverse()
            for j in range(len(b)):
                if b[j] == '1':
                    b[j] = '0'
                else:
                    b[j] = '1'
            a = list(map(str, "".join(a) + '0' + "".join(b)))
        a = a[0:l]

        # get checksum
        checksum = a[:]
        while len(checksum) % 2 == 0:
            newChecksum = []
            for i in range(0, len(checksum), 2):
                if checksum[i] == checksum[i+1]:
                    newChecksum.append('1')
                else:
                    newChecksum.append('0')
            checksum = newChecksum[:]
        print(f"Correct checksum for disk of length {l}: {"".join(checksum)}")


    def solve2(self):
        print("--- Part Two ---")
        # l = 20
        l = 35651584

        # generate data
        a = [False] * l
        for i in range(len(self.ins)):
            a[i] = True if self.ins[i] == '1' else False
        curL = len(self.ins)
        while curL < l:
            # print(curL)
            a[curL] = False
            for li in range(0, curL):
                if curL+li+1 >= l:
                    break
                a[curL+li+1] = not a[curL-li-1]
            curL += curL+1

        # get checksum
        checksum = a[:]
        while len(checksum) % 2 == 0:
            newChecksum = []
            for i in range(0, len(checksum), 2):
                if checksum[i] == checksum[i+1]:
                    newChecksum.append(True)
                else:
                    newChecksum.append(False)
            checksum = newChecksum[:]
        print(f"Correct checksum for disk of length {l}: ", end="")
        for b in checksum:
            if b:
                print('1', end="")
            else:
                print('0', end="")
        print()

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
