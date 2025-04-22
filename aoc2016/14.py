QUIZ_NUMBER = "14"
import hashlib

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        # solution.solve1()
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
        i = 0
        curKey = 0
        while curKey < 64:
            t = self.ins + str(i)
            m = hashlib.md5()
            m.update(t.encode())
            h = m.hexdigest()

            c = None
            foundTriple = False
            for j in range(1, len(h)-1):
                if h[j-1] == h[j] == h[j+1]:
                    c = h[j]
                    foundTriple = True
                    break
                    # print(f"found triple (key: {t})... checking for five-ple...")
            if foundTriple:
                j = i+1
                foundKey = False
                while i+1000 >= j and not foundKey:
                    t2 = self.ins + str(j)
                    m2 = hashlib.md5()
                    m2.update(t2.encode())
                    h2 = m2.hexdigest()
                    for k in range(2, len(h2)-2):
                        if h2[k-2] == h2[k-1] == h2[k] == h2[k+1] == h2[k+2] == c:
                            print(f"found five-ple: {i}->{j}: {c}")
                            curKey += 1
                            foundKey = True
                            break
                    j += 1
            i += 1
        print(f"64th key (index {i-1}): {h}")

    def solve2(self):
        print("--- Part Two ---")

        print("creating hashes...")
        hashes = []
        for i in range(30000): # produce 30000 hashes...
            t = self.ins + str(i)
            m = hashlib.md5()
            m.update(t.encode())
            h = m.hexdigest()
            for _ in range(2016):
                m = hashlib.md5()
                m.update(h.encode())
                h = m.hexdigest()
            hashes.append(h)

        print("finding 64th key...")
        i = 0
        curKey = 0
        while curKey < 64:
            h = hashes[i]
            c = None
            foundTriple = False
            for j in range(1, len(h)-1):
                if h[j-1] == h[j] == h[j+1]:
                    c = h[j]
                    foundTriple = True
                    break
                    # print(f"found triple (key: {t})... checking for five-ple...")
            if foundTriple:
                j = i+1
                foundKey = False
                while i+1000 >= j and not foundKey:
                    h2 = hashes[j]
                    for k in range(2, len(h2)-2):
                        if h2[k-2] == h2[k-1] == h2[k] == h2[k+1] == h2[k+2] == c:
                            print(f"found five-ple: {i}->{j}: {c}")
                            curKey += 1
                            foundKey = True
                            break
                    j += 1
            i += 1
        print(f"64th key (index {i-1}): {h}")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
