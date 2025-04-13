QUIZ_NUMBER = "8"
import math

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        # solution.solve1()
        # solution.solve2_preprocess()
        solution.solve2_postprocess()

    def test():
        Solution.run(QUIZ_NUMBER + ".2.ex.in")

    def __init__(self, fileName):
        self.fileName = fileName
        self.ins = []
        fp = open(fileName, 'r')
        arr = fp.read().split('\n')
        self.ins.append(arr[0])
        for i in range(2, len(arr)):
            if not arr[i]:
                break
            line = arr[i].split()
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        step = 0
        maxStep = len(self.ins[0])
        stepSeq = self.ins[0]
        curNode = "AAA"

        nodes = dict()
        for i in range(1, len(self.ins)):
            nodes[self.ins[i][0]] = [self.ins[i][1], self.ins[i][2]]

        while curNode != "ZZZ":
            next = stepSeq[step % maxStep]
            if next == 'L':
                curNode = nodes[curNode][0]
            elif next == 'R':
                curNode = nodes[curNode][1]
            step += 1

        print("Number of steps required to reach 'ZZZ':", step)

    def solve2_preprocess(self):
        print("--- Part Two ---")
        maxStep = len(self.ins[0])
        stepSeq = self.ins[0]
        curNodes = []
        startNodes = []
        startNodeSteps = []

        nodes = dict()
        for i in range(1, len(self.ins)):
            nodes[self.ins[i][0]] = [self.ins[i][1], self.ins[i][2]]
            # get all starting nodes
            if self.ins[i][0][2] == 'A':
                startNodes.append(self.ins[i][0])
        for startNode in startNodes:
            step = 0
            print("Starting node:", startNode)
            curNodes.append(startNode)
            nodeSteps = []
            while curNodes:
                nextNodes = []
                testStep = []
                while curNodes:
                    curNode = curNodes.pop(0)
                    next = stepSeq[step % maxStep]
                    if next == 'L':
                        nextNodes.append(nodes[curNode][0])
                    elif next == 'R':
                        nextNodes.append(nodes[curNode][1])
                for next in nextNodes:
                    # if next[2] != 'Z':
                        # curNodes = nextNodes[::]
                        # break
                    if next[2] == 'Z':
                        # print("found Z, cur step:", step)
                        nodeSteps.append(step+1)
                    if step < 10000000:
                        curNodes = nextNodes[::]
                step += 1
            startNodeSteps.append(nodeSteps)
        diff = []
        firstEnds = []
        for i in range(0, len(startNodeSteps)):
            firstEnds.append(startNodeSteps[i][0])
            diffStep = []
            for j in range(1, len(startNodeSteps[i])):
                curDiff = startNodeSteps[i][j]-startNodeSteps[i][j-1]
                if not diffStep or diffStep[-1] != curDiff:
                    diffStep.append(curDiff)
            diff.append(diffStep[::])
        print(diff)
        print(firstEnds)
        # print("Number of steps required for all nodes to reach nodes ending in 'Z':", step)

    def solve2_postprocess(self):
        steps = [21409, 14363, 15989, 16531, 19241, 19783]
        # print((math.prod(steps))//math.gcd(*steps))
        lcm = 1
        for step in steps:
            lcm = lcm*step//math.gcd(lcm, step)
        print(lcm)

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
