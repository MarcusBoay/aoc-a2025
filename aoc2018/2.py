QUIZ_NUMBER = "2"

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
            line = arr[i]
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        totals = [0, 0] # index 0 == number of box IDs where a letter appears exactly twice, index 1 == number of box IDs where a letter appears exactly thrice

        for boxID in self.ins:
            freq = dict()
            for letter in boxID:
                if letter not in freq:
                    freq[letter] = 0
                freq[letter] += 1
            seen = [False, False] # index 0 == found letter(s) that appear exactly twice, index 1 == found letter(s) that appear exactly thrice
            for letter in freq:
                if freq[letter] == 2:
                    seen[0] = True
                elif freq[letter] == 3:
                    seen[1] = True
            if seen[0]:
                totals[0] += 1
            if seen[1]:
                totals[1] += 1

        print("Checksum:", totals[0]*totals[1])

    def solve2(self):
        print("--- Part Two ---")
        def findCommonLetters():
            commonLetters = []
            for i in range(len(self.ins)):
                for j in range(i+1, len(self.ins)):
                    diff = 0 # number of differences in both IDs
                    for ci in range(0, len(self.ins[i])):
                        if self.ins[i][ci] != self.ins[j][ci]:
                            diff += 1
                    if diff == 1:
                        for ci in range(0, len(self.ins[i])):
                            if self.ins[i][ci] == self.ins[j][ci]:
                                commonLetters.append(self.ins[i][ci])
                        return "".join(commonLetters)
        print("Common letters between two correct box IDs:", findCommonLetters())


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
