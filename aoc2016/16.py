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

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
