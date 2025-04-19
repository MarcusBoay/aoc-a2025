QUIZ_NUMBER = "14"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")
        self.elementsN = 256
        self.elements = []
        for i in range(256):
            self.elements.append(i)

    def knotHash(self, keyString):
        # convert each character to ASCII code
        ASCIICodes = []
        for c in keyString:
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
        return int(hexStr, 16)

    def solve1(self):
        print("--- Part One ---")
        totalSetBits = 0
        for i in range(128):
            s = self.ins + "-" + str(i)
            knotHash = self.knotHash(s)
            while knotHash:
                totalSetBits += 1
                knotHash &= knotHash-1

        print(f"Number of squares used: {totalSetBits}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
