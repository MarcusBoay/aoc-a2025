QUIZ_NUMBER = "7"

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
        self.ins = list(map(str, fp.read().split('\n')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")

        totalSupportedIPs = 0
        for ip in self.ins:
            foundFirstMatch = False
            shouldFind = True
            supportsTLS = True
            hasABBA = False
            for i in range(1, len(ip)):
                c = ip[i]
                if c == '[':
                    shouldFind = False
                    foundFirstMatch = False
                elif c == ']':
                    shouldFind = True
                    foundFirstMatch = False
                elif not foundFirstMatch and c == ip[i-1]:
                    foundFirstMatch = True
                elif foundFirstMatch and i > 2 and ip[i-1] not in "[]" and ip[i-2] not in "[]" and c == ip[i-3]:
                    if not shouldFind:
                        supportsTLS = False
                        break
                    hasABBA = True
                    foundFirstMatch = False
                else:
                    foundFirstMatch = False

            if supportsTLS and hasABBA:
                totalSupportedIPs += 1

        print("Number of IPs that support TLS:", totalSupportedIPs)


    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
