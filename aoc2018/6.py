QUIZ_NUMBER = "6"

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
            line = list(map(int, arr[i].split(", ")))
            line.append(chr(i+ord('A')))
            self.ins.append(tuple(line))
        fp.close()
        print("===", self.fileName, "===")
        print(self.ins)

    def solve1(self):
        print("--- Part One ---")

        q = self.ins[:]
        seen = set()
        areas = dict()
        for ijc in q:
            # seen.add((ijc[0], ijc[1]))
            areas[ijc[2]] = 1

        reps = 500
        while reps:
            reps -= 1
            qn = len(q)
            conflict = set()
            curSeen = set()
            curSeenPos = set()
            while qn:
                qn -= 1
                ijc = q.pop(0)
                if (ijc[0],ijc[1]) in seen:
                    continue
                if (ijc[0],ijc[1]) in curSeenPos:
                    conflict.add((ijc[0],ijc[1]))
                    continue
                seen.add((ijc[0],ijc[1]))
                curSeen.add(ijc)
                curSeenPos.add((ijc[0],ijc[1]))
                ni,nj = ijc[0]-1,ijc[1]
                if (ni,nj) not in seen:
                    q.append((ni,nj,ijc[2]))
                ni,nj = ijc[0]+1,ijc[1]
                if (ni,nj) not in seen:
                    q.append((ni,nj,ijc[2]))
                ni,nj = ijc[0],ijc[1]-1
                if (ni,nj) not in seen:
                    q.append((ni,nj,ijc[2]))
                ni,nj = ijc[0],ijc[1]+1
                if (ni,nj) not in seen:
                    q.append((ni,nj,ijc[2]))
            for ijc in curSeen:
                if (ijc[0],ijc[1]) not in conflict:
                    areas[ijc[2]] += 1
        print(areas)
        for a in areas:
            print(a, areas[a])


    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
