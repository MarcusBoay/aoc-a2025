QUIZ_NUMBER = "5"

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
            self.ins.append(arr[i][:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        numberOfNiceStrings = 0
        for s in self.ins:
            hasNaughtyString = False
            hasTwice = False
            vowels = 0
            for i in range(len(s)):
                c = s[i]
                if c in "aeiou":
                    vowels += 1

                if i > 0 and s[i-1] == s[i]:
                    hasTwice = True

                if i > 0 and s[i-1:i+1] in ["ab", "cd", "pq", "xy"]:
                    hasNaughtyString = True
                    break

            if vowels >= 3 and hasTwice and not hasNaughtyString:
                numberOfNiceStrings += 1

        print("Number of nice strings:", numberOfNiceStrings)

    def solve2(self):
        print("--- Part Two ---")
        numberOfNiceStrings = 0
        for s in self.ins:
            hasABA = False
            for i in range(1, len(s)-1):
                if s[i-1] == s[i+1]:
                    hasABA = True
                    break
            hasABAB = False
            for i in range(0, len(s)-1):
                for j in range(i+2, len(s)-1):
                    if s[i] == s[j] and s[i+1] == s[j+1]:
                        hasABAB = True
            if hasABA and hasABAB:
                numberOfNiceStrings += 1

        print("Number of nice strings:", numberOfNiceStrings)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
