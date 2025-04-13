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

        totalSupportedIPs = 0
        for ip in self.ins:
            ABAs = set()
            BABs = set()
            isWithin = False
            i = 1
            while i < len(ip)-1:
                c = ip[i]
                if c == '[':
                    isWithin = True
                    i += 2
                    continue
                elif c == ']':
                    isWithin = False
                    i += 2
                    continue

                if ip[i-1] == ip[i+1]:
                    print(ip[i-1:i+2])
                    if not isWithin:
                        ABAs.add(ip[i-1:i+2])
                    else:
                        BABs.add(ip[i-1:i+2])
                i += 1

            supportsSSL = False
            for ABA in ABAs:
                BAB = ABA[1] + ABA[0] + ABA[1]
                if BAB in BABs:
                    supportsSSL = True
            if supportsSSL:
                totalSupportedIPs += 1

        print("Numbers of IPs that support SSL:", totalSupportedIPs)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
