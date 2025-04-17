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

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
