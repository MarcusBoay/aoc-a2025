QUIZ_NUMBER = "6"

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
        self.ins = list(map(str, fp.read().split('\n')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        result = ""
        for j in range(len(self.ins[0])):
            charFreq = dict()
            mostFreqChar = '.'
            n = 0
            for i in range(len(self.ins)):
                if self.ins[i][j] not in charFreq:
                    charFreq[self.ins[i][j]] = 0
                charFreq[self.ins[i][j]] += 1

            for c in charFreq:
                if n < charFreq[c]:
                    mostFreqChar = c
                    n = charFreq[c]
            result += mostFreqChar
        print("Error corrected version of the message:", result)

    def solve2(self):
        print("--- Part Two ---")
        result = ""
        for j in range(len(self.ins[0])):
            charFreq = dict()
            for i in range(len(self.ins)):
                if self.ins[i][j] not in charFreq:
                    charFreq[self.ins[i][j]] = 0
                charFreq[self.ins[i][j]] += 1

            leastFreqChar = '.'
            n = len(self.ins)
            for c in charFreq:
                if n > charFreq[c]:
                    leastFreqChar = c
                    n = charFreq[c]
            result += leastFreqChar
        print("Original message:", result)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
