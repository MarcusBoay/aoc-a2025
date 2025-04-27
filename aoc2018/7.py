QUIZ_NUMBER = "7"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.children = dict()
        self.parents = dict()
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            if line[0] not in self.children:
                self.children[line[0]] = []
            self.children[line[0]].append(line[1])
            if line[1] not in self.parents:
                self.parents[line[1]] = []
            self.parents[line[1]].append(line[0])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        # find first step to complete
        startNodes = []
        for parent in self.children:
            if parent not in self.parents:
                startNodes.append(parent)

        seen = set()
        q = startNodes[:]
        steps = ""
        while q:
            toProcess = []
            # shortlist nodes to process
            for c in q:
                # only shortlist current node if its parents have all been processed
                # no parents, i.e: root node. process it unconditionally
                shouldAdd = True
                if c in self.parents:
                    for p in self.parents[c]:
                        if p not in seen:
                            shouldAdd = False
                if shouldAdd:
                    toProcess.append(c)

            # alphabetically sort shortlisted nodes to process
            toProcess.sort()
            cur = toProcess.pop(0)
            for i in range(len(q)):
                if cur == q[i]:
                    q.pop(i)
                    break
            if cur not in seen:
                seen.add(cur)
                steps += cur

            # add children to process next
            if cur in self.children:
                for c in self.children[cur]:
                    q.append(c)

        print(f"Steps to complete in order: {steps}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
