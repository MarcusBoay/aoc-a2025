QUIZ_NUMBER = "20"

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
            line = list(map(int, arr[i].split('-')))
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        ip = 0
        while True:
            isBlocked = False
            for r in self.ins:
                if r[0] <= ip <= r[1]:
                    ip = r[1]+1
                    isBlocked = True
                    break
            if not isBlocked:
                break
        print(f"Lowest-valued IP that is not blocked: {ip}")

    def solve2(self):
        print("--- Part Two ---")
        ip = 0
        ips = 0

        # maxIP = 10
        maxIP = 4294967295+1
        while ip < maxIP:
            isBlocked = False
            for r in self.ins:
                if r[0] <= ip <= r[1]:
                    ip = r[1]+1
                    # print(f"blocked by {r}... new ip: {ip}")
                    isBlocked = True
                    break

            if not isBlocked:
                nextBlockIP = maxIP
                nextIP = ip
                for r in self.ins:
                    if r[0] > ip and r[0] < nextBlockIP:
                        nextBlockIP = r[0]
                        nextIP = r[1]
                ips += nextBlockIP-ip
                ip = nextIP+1
        print(f"Number of IPs allowed by the blacklist: {ips}")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
