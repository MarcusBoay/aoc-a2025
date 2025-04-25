QUIZ_NUMBER = "24"

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
        self.ins = list(map(list[str], fp.read().split('\n')))
        fp.close()
        print("===", self.fileName, "===")
        self.pos = dict() # 0, (i, j)
        for i in range(len(self.ins)):
            for j in range(len(self.ins[i])):
                col = self.ins[i][j]
                if col.isdigit():
                    self.pos[col] = (i, j)

    def solve1(self):
        print("--- Part One ---")

        # get edges from each node to every node
        self.nodes = [[None for j in range(len(self.pos))] for i in range(len(self.pos))]
        for p in self.pos:
            q = [self.pos[p]]
            steps = 0
            numbersSeen = set()
            seen = set() # coords seen
            seen.add(self.pos[p])

            doneProcessingP = False
            while q:
                qn = len(q)
                while qn:
                    qn -= 1
                    cur = q.pop(0)
                    if self.ins[cur[0]][cur[1]].isdigit():
                        # print(f"from {p}, reached {self.ins[cur[0]][cur[1]]}, takes {steps} steps...")
                        numbersSeen.add(self.ins[cur[0]][cur[1]])
                        self.nodes[int(p)][int(self.ins[cur[0]][cur[1]])] = steps
                    if (len(numbersSeen) == len(self.pos)):
                        doneProcessingP = True
                        break

                    ni,nj = cur[0]-1,cur[1]
                    if ni >= 0 and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                    ni,nj = cur[0]+1,cur[1]
                    if ni < len(self.ins) and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                    ni,nj = cur[0],cur[1]-1
                    if nj >= 0 and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                    ni,nj = cur[0],cur[1]+1
                    if nj < len(self.ins[ni]) and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                if doneProcessingP:
                    break
                steps += 1
        # for row in nodes:
        #     print(row)

        self.seen = set()
        self.shortestPath = 99999999999
        def backtrack(i, steps):
            if len(self.seen) == len(self.pos):
                self.shortestPath = min(self.shortestPath, steps)

            for j in range(len(self.nodes)):
                if j not in self.seen:
                    self.seen.add(j)
                    backtrack(j, steps+self.nodes[i][j])
                    self.seen.remove(j)
        backtrack(0, 0)

        print(f"Shortest path to visit all nodes: {self.shortestPath}")

    def solve2(self):
        print("--- Part Two ---")

        # get edges from each node to every node
        self.nodes = [[None for j in range(len(self.pos))] for i in range(len(self.pos))]
        for p in self.pos:
            q = [self.pos[p]]
            steps = 0
            numbersSeen = set()
            seen = set() # coords seen
            seen.add(self.pos[p])

            doneProcessingP = False
            while q:
                qn = len(q)
                while qn:
                    qn -= 1
                    cur = q.pop(0)
                    if self.ins[cur[0]][cur[1]].isdigit():
                        # print(f"from {p}, reached {self.ins[cur[0]][cur[1]]}, takes {steps} steps...")
                        numbersSeen.add(self.ins[cur[0]][cur[1]])
                        self.nodes[int(p)][int(self.ins[cur[0]][cur[1]])] = steps
                    if (len(numbersSeen) == len(self.pos)):
                        doneProcessingP = True
                        break

                    ni,nj = cur[0]-1,cur[1]
                    if ni >= 0 and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                    ni,nj = cur[0]+1,cur[1]
                    if ni < len(self.ins) and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                    ni,nj = cur[0],cur[1]-1
                    if nj >= 0 and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                    ni,nj = cur[0],cur[1]+1
                    if nj < len(self.ins[ni]) and (ni,nj) not in seen and self.ins[ni][nj] != '#':
                        seen.add((ni,nj))
                        q.append((ni,nj))
                if doneProcessingP:
                    break
                steps += 1
        # for row in nodes:
        #     print(row)

        self.seen = set()
        self.shortestPathWithReturn = 99999999999
        def backtrack(i, steps):
            if len(self.seen) == len(self.pos):
                self.shortestPathWithReturn = min(self.shortestPathWithReturn, steps+self.nodes[0][i])

            for j in range(len(self.nodes)):
                if j not in self.seen:
                    self.seen.add(j)
                    backtrack(j, steps+self.nodes[i][j])
                    self.seen.remove(j)
        backtrack(0, 0)

        print(f"Shortest path to visit all nodes: {self.shortestPathWithReturn}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
