QUIZ_NUMBER = "10"

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
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        sequence = list(map(str, self.ins[::]))
        for i in range(40):
            curDigit = None
            quantity = 0
            nextSequence = []
            while sequence:
                if not curDigit:
                    curDigit = sequence.pop(0)
                    quantity = 1
                    continue
                nextDigit = sequence.pop(0)
                if curDigit == nextDigit:
                    quantity += 1
                else:
                    nextSequence.append(str(quantity))
                    nextSequence.append(curDigit)
                    curDigit = nextDigit
                    quantity = 1
            nextSequence.append(str(quantity))
            nextSequence.append(curDigit)
            sequence = nextSequence[::]
            # print("ite:", i+1, "sequence:", "".join(sequence))
        # print("Result after iterating 40 times:", "".join(sequence))
        print("Length of result:", len(sequence))



    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
