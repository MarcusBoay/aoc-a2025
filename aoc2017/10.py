QUIZ_NUMBER = "10"

class Solution:
    def run(elementsN = 256, fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(elementsN, fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(5, QUIZ_NUMBER + ".ex.in")

    def __init__(self, elementsN, fileName):
        self.lengths = []
        self.elementsN = elementsN
        self.elements = []
        for i in range(elementsN):
            self.elements.append(i)
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.lengths = list(map(int, fp.read().split(',')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        skipSize = 0
        position = 0
        for l in self.lengths:
            # reverse order of length, l of elements in the list at position
            i, j = position, position+l-1
            while i < j:
                self.elements[i%self.elementsN], self.elements[j%self.elementsN] = self.elements[j%self.elementsN], self.elements[i%self.elementsN]
                i += 1
                j -= 1

            # move current position forward by l + skip size, s
            position += l + skipSize

            # increment s by 1
            skipSize += 1
            # print(f"Order of elements after the {skipSize} operation: {self.elements}")
        print(f"The result of multiplying the first two numbers in the list: {self.elements[0]*self.elements[1]}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
