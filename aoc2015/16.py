QUIZ_NUMBER = "16"

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
        self.ins.append('0')
        for i in range(0, len(arr)):
            line = arr[i].split()
            things = line[1].split(",")
            thingDict = dict()
            for thing in things:
                thing = thing.split(':')
                thingDict[thing[0]] = int(thing[1])
            line = [int(line[0]), thingDict]
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")
        self.match = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }

    def solve1(self):
        print("--- Part One ---")
        possibleAunt = []
        for i in range(1, 501):
            curMatch = self.match.copy()
            isPossibleAunt = True
            for thing in self.ins[i][1]:
                if curMatch[thing] != self.ins[i][1][thing]:
                    isPossibleAunt = False
                    break
            if isPossibleAunt:
                possibleAunt.append(i)
        print("Possible aunts:", possibleAunt)

    def solve2(self):
        print("--- Part Two ---")
        possibleAunt = []
        for i in range(1, 501):
            curMatch = self.match.copy()
            isPossibleAunt = True
            for thing in self.ins[i][1]:
                auntThingN = self.ins[i][1][thing]
                if thing in ["cats", "trees"] and \
                   curMatch[thing] >= auntThingN:
                    isPossibleAunt = False
                    break
                elif thing in ["pomeranians", "goldfish"] and \
                     curMatch[thing] <= auntThingN:
                    isPossibleAunt = False
                    break
                elif thing not in ["cats", "trees", "pomeranians", "goldfish"] and \
                     curMatch[thing] != auntThingN:
                    isPossibleAunt = False
                    break
            if isPossibleAunt:
                possibleAunt.append(i)
        print("Possible aunts:", possibleAunt)

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
