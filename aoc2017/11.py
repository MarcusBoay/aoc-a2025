QUIZ_NUMBER = "11"

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
            line = arr[i].split(',')
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        actions = dict()
        actions["n"] = (0, -1)
        actions["s"] = (0, 1)
        actions["ne"] = (1, -0.5)
        actions["sw"] = (-1, 0.5)
        actions["se"] = (1, 0.5)
        actions["nw"] = (-1, -0.5)

        # take original steps
        for row in self.ins:
            coords = [0, 0]
            for step in row:
                coords[0] += actions[step][0]
                coords[1] += actions[step][1]

            seen = set()
            q = []
            q.append((0, 0))
            steps = 0
            found = False
            while not found:
                qn = len(q)
                while qn:
                    qn -= 1
                    cur = q.pop(0)
                    seen.add(cur)
                    if cur[0] == coords[0] and cur[1] == coords[1]:
                        print(f"Number of steps to get to {coords}: {steps}")
                        found = True
                    for a in actions:
                        next = (cur[0] + actions[a][0], cur[1] + actions[a][1])
                        if next not in seen:
                            seen.add(next)
                            q.append(next)
                steps += 1

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
