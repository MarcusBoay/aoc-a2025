QUIZ_NUMBER = "19"
import re

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
        self.ins = arr[:]
        self.replacements = dict()
        self.startingMolecule = ""
        readStartingMolecule = False
        for i in range(0, len(arr)):
            if len(arr[i]) == 0:
                readStartingMolecule = True
                continue
            if not readStartingMolecule:
                line = arr[i].split(' => ')
                if line[0] not in self.replacements:
                    self.replacements[line[0]] = []
                self.replacements[line[0]].append(line[1])
            else:
                self.startingMolecule = arr[i][:]
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        distinctMolecules = set()
        for r in self.replacements:
            mIter = re.finditer(r, self.startingMolecule)
            try:
                while True:
                    m = next(mIter)
                    for rr in self.replacements[r]:
                        newMolecule = self.startingMolecule[0:m.start()] + \
                            rr + \
                            self.startingMolecule[m.end()::]
                        distinctMolecules.add(newMolecule)
                        # print(newMolecule)
            except:
                pass
        print(f"Number of distinct molecules that can be created: {len(distinctMolecules)}")

    def solve2(self):
        print("--- Part Two ---")
        terminals = set()
        allEnds = set()
        allR = set()
        for r in self.replacements:
            allR.add(r)
        for r in self.replacements:
            for longestReplacement in self.replacements[r]:
                cur = ""
                allCur = set()
                for c in longestReplacement:
                    if c.islower():
                        cur += c
                    else:
                        if cur:
                            allCur.add(cur)
                        cur = c
                allCur.add(cur)
                allEnds.add(cur)
                for c in allCur:
                    if c not in allR:
                        terminals.add(c)
        print(f"Replacement terminal molecules: {terminals}")
        terminalEnds = set()
        for t in terminals:
            if t in allEnds:
                terminalEnds.add(t)
        print(f"Replacement terminal molecules that are ends: {terminalEnds}")

        splits = []
        mIter = re.finditer(list(terminalEnds)[0], self.startingMolecule)
        prevEnd = 0
        try:
            while True:
                m = next(mIter)
                splits.append(self.startingMolecule[prevEnd:m.end()])
                prevEnd = m.end()
        except:
            pass
        if self.startingMolecule[prevEnd::]:
            splits.append(self.startingMolecule[prevEnd::])
        # for m in splits:
        #     print(m)

        self.reverseReplacements = dict()
        for i in range(len(self.ins)):
            if len(self.ins[i]) == 0:
                break
            line = self.ins[i].split(' => ')
            if line[1] not in self.reverseReplacements:
                self.reverseReplacements[line[1]] = []
            self.reverseReplacements[line[1]].append(line[0])
        replacements = 0
        for i in range(len(splits)):
            if splits[i] in self.reverseReplacements:
                replacements += 1
                print(f"replacing {splits[i]} for {self.reverseReplacements[splits[i]][0]}")
                splits[i] = self.reverseReplacements[splits[i]][0]
        print(splits)
        didReplace = True
        while didReplace:
            didReplace = False
            for i in range(len(splits)):
                s = splits[i]
                longestReplacementN = 0
                longestReplacement = ""
                for r in self.reverseReplacements:
                    if s.find(r) >= 0 and len(r) > longestReplacementN:
                        print(r)
                        longestReplacementN = len(r)
                        longestReplacement = r
                        didReplace = True
                if didReplace:
                    si = s.find(longestReplacement)
                    print(longestReplacement)
                    print(f"replacing {longestReplacement} in {splits[i]} for {self.reverseReplacements[longestReplacement][0]}")
                    splits[i] = s[0:si] + self.reverseReplacements[longestReplacement][0] + s[si+longestReplacementN::]
                    replacements += 1
                    break
                    # exit()
        print(splits)
        newMolecule = "".join(splits)
        didReplace = True
        while didReplace:
            didReplace = False
            # for i in range(len(splits)):
            s = newMolecule
            longestReplacementN = 0
            longestReplacement = ""
            for r in self.reverseReplacements:
                if s.find(r) >= 0 and len(r) > longestReplacementN:
                    print(r)
                    longestReplacementN = len(r)
                    longestReplacement = r
                    didReplace = True
            if didReplace:
                si = s.find(longestReplacement)
                print(longestReplacement)
                print(f"replacing {longestReplacement} in {s} for {self.reverseReplacements[longestReplacement][0]}")
                newMolecule = s[0:si] + self.reverseReplacements[longestReplacement][0] + s[si+longestReplacementN::]
                replacements += 1
        print(newMolecule, replacements)


def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
