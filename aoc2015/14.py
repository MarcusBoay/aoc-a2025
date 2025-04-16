QUIZ_NUMBER = "14"

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
        n = 2503
        # 0 4 7 14
        nameMap = dict()
        speed = [0] * len(self.ins)
        period = [0] * len(self.ins)
        rest = [0] * len(self.ins)
        for i in range(len(self.ins)):
            nameMap[i] = self.ins[i][0]
            speed[i] = int(self.ins[i][3])
            period[i] = int(self.ins[i][6])
            rest[i] = int(self.ins[i][13])
        dist = [0] * len(self.ins)
        cur = period[:]
        for i in range(n):
            for j in range(len(speed)):
                # process rest first
                if -cur[j] >= rest[j]:
                    cur[j] = period[j]
                elif cur[j] <= 0:
                    cur[j] -= 1

                # process fly
                if cur[j] > 0:
                    dist[j] += speed[j]
                    cur[j] -= 1
        print("Distance travelled by all reindeer:", dist)
        print("Distance travelled by winning reindeer:", max(dist))


    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
