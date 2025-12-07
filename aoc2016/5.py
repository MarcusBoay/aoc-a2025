QUIZ_NUMBER = "5"
import hashlib

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
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")

        password = ""
        i = 0
        while len(password) < 8:
            t = self.ins + str(i)
            m = hashlib.md5()
            m.update(t.encode())
            h = m.hexdigest()
            if h[0:5] == "00000":
                password += h[5]
            i += 1
        print("Password:", password)

    def solve2(self):
        print("--- Part Two ---")

        password = ['.' for i in range(8)]
        i = 0
        filled = 0
        while filled < 8:
            t = self.ins + str(i)
            m = hashlib.md5()
            m.update(t.encode())
            h = m.hexdigest()
            if h[0:5] == "00000" and ord('0') <= ord(h[5]) < ord('8') and password[int(h[5])] == '.':
                password[int(h[5])] = h[6]
                filled += 1
            i += 1
        print("Password:", "".join(password))

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
