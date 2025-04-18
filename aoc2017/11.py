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

        for row in self.ins:
            # take original steps
            coords = [0, 0]
            for i in range(len(row)):
                step = row[i]
                coords[0] += actions[step][0]
                coords[1] += actions[step][1]
            print(f"total steps taken: {len(row)}")

            # find min steps to coords
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
        actions = dict()
        actions["n"] = (0, -1)
        actions["s"] = (0, 1)
        actions["ne"] = (1, -0.5)
        actions["sw"] = (-1, 0.5)
        actions["se"] = (1, 0.5)
        actions["nw"] = (-1, -0.5)

        for row in self.ins:
            # take original steps and get max coords
            coords = [0, 0]
            maxStep = 0
            for i in range(len(row)):
                step = row[i]
                coords[0] += actions[step][0]
                coords[1] += actions[step][1]

                # find min steps to cur coords
                steps = 0
                if coords[0] < 0:
                    # xw
                    steps += abs(coords[0])
                    if coords[1] < 0:
                        # nw
                        steps += coords[1] - coords[0]/2
                    else:
                        # sw
                        steps += coords[1] + coords[0]/2
                else:
                    # xe
                    steps += coords[0]
                    if coords[1] < 0:
                        # ne
                        steps += coords[1] + coords[0]/2
                    else:
                        # se
                        steps += coords[1] - coords[0]/2
                maxStep = max(maxStep, steps)

            print(f"Reached max coords at step {maxStep}")


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
