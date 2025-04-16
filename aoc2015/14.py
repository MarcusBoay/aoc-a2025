QUIZ_NUMBER = "14"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in", n=2503):
        solution = Solution(fileName, n)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in", 1000)

    def __init__(self, fileName, n):
        self.ins = []
        self.n = n
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
        for i in range(self.n):
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
        print("Distance travelled by all reindeer after", self.n,"seconds:", dist)
        print("Distance travelled by winning reindeer after", self.n,"seconds:", max(dist))


    def solve2(self):
        print("--- Part Two ---")
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
        points = [0] * len(self.ins)
        cur = period[:]
        for i in range(self.n):
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
            curWinner = 0
            for j in range(len(points)):
                if dist[j] > curWinner:
                    curWinner = dist[j]
            ties = []
            for j in range(len(points)):
                if dist[j] == curWinner:
                    ties.append(j)
            for j in ties:
                points[j] += 1
        print("Points of the all reindeer after", self.n,"seconds:", points)
        print("Points of the winning reindeer after", self.n,"seconds:", max(points))

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
