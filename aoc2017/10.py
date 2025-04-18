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
        self.ins = fp.read()
        self.lengths = list(map(int, self.ins.split(',')))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        skipSize = 0
        position = 0
        elements = self.elements[:]
        for l in self.lengths:
            # reverse order of length, l of elements in the list at position
            i, j = position, position+l-1
            while i < j:
                elements[i%self.elementsN], elements[j%self.elementsN] = elements[j%self.elementsN], elements[i%self.elementsN]
                i += 1
                j -= 1

            # move current position forward by l + skip size, s
            position += l + skipSize

            # increment s by 1
            skipSize += 1
            # print(f"Order of elements after the {skipSize} operation: {self.elements}")
        print(f"The result of multiplying the first two numbers in the list: {elements[0]*elements[1]}")

    def solve2(self):
        print("--- Part Two ---")
        # convert each character to ASCII code
        ASCIICodes = []
        for c in self.ins:
            ASCIICodes.append(ord(c))

        # append this static sequence
        ss = [17, 31, 73, 47, 23]
        for s in ss:
            ASCIICodes.append(s)

        # run 64 rounds of solve1()
        skipSize = 0
        position = 0
        elements = self.elements[:]
        for _ in range(64):
            for l in ASCIICodes:
                # reverse order of length, l of elements in the list at position
                i, j = position, position+l-1
                while i < j:
                    elements[i%self.elementsN], elements[j%self.elementsN] = elements[j%self.elementsN], elements[i%self.elementsN]
                    i += 1
                    j -= 1

                # move current position forward by l + skip size, s
                position += l + skipSize

                # increment s by 1
                skipSize += 1

        # reduce the numbers to form a dense hash
        denseHash = []
        for i in range(16):
            curNumber = 0
            for j in range(16):
                curNumber ^= elements[i*16+j]
            denseHash.append(curNumber)

        # represent the dense hash in hexadecimal notation
        hexStr = ""
        for d in denseHash:
            hexStr += str(hex(d))[2:4]
        print(f"Knot Hash: {hexStr}")


def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
