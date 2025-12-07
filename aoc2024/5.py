QUIZ_NUMBER = "5"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.rules = dict()
        self.pagesToProduce = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        parsed = [False, False]
        for i in range(0, len(arr)):
            if not parsed[0]:
                if not arr[i]:
                    parsed[0] = True
                else:
                    line = arr[i].split('|')
                    if line[0] not in self.rules:
                        self.rules[line[0]] = set()
                    self.rules[line[0]].add(line[1])
            elif not parsed[1]:
                if not arr[i]:
                    parsed[1] = True
                else:
                    self.pagesToProduce.append(arr[i].split(','))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        middlePages = []
        self.badUpdates = []
        for pages in self.pagesToProduce:
            isRuleBreaking = False
            for i in range(len(pages)):
                for j in range(i+1, len(pages)):
                    if (pages[i] in self.rules and \
                        pages[j] not in self.rules[pages[i]]) or \
                       (pages[j] in self.rules and \
                        pages[i] in self.rules[pages[j]]):
                        isRuleBreaking = True
                        break
                if isRuleBreaking:
                    self.badUpdates.append(pages[::])
                    break
            if not isRuleBreaking:
                mid = int(pages[len(pages)//2])
                middlePages.append(mid)
        print("Sum of middle pages:", sum(middlePages))

    def solve2(self):
        print("--- Part Two ---")
        middlePages = []
        for pages in self.badUpdates:
            didChange = True
            while didChange:
                didChange = False
                for i in range(len(pages)):
                    for j in range(i+1, len(pages)):
                        if (pages[j] in self.rules and \
                            pages[i] in self.rules[pages[j]]):
                            didChange = True
                            pages[i], pages[j] = pages[j], pages[i]
                            break
                    if didChange:
                        break
            mid = int(pages[len(pages)//2])
            middlePages.append(mid)
        print("Sum of middle pages after correctly ordering bad updates:", sum(middlePages))

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
