QUIZ_NUMBER = "8"

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
        self.ins = list(map(int, fp.read().split()))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        self.metadataSum = 0
        def postorder(i = 0):
            # get number of children
            n = self.ins[i]
            i += 1
            # get number of metadata entries
            m = self.ins[i]
            i += 1
            # iterate over all children
            for _ in range(n):
                i = postorder(i)
            # get all metadata entries
            for j in range(i, i+m):
                self.metadataSum += self.ins[j]

            return i+m
        postorder()
        print("Sum of all metadata entries:", self.metadataSum)


    def solve2(self):
        print("--- Part Two ---")
        def postorder(i = 0):
            # get number of children
            n = self.ins[i]
            i += 1
            # get number of metadata entries
            m = self.ins[i]
            i += 1
            # iterate over all children
            childMetadata = []
            for _ in range(n):
                (i, metadata) = postorder(i)
                childMetadata.append(metadata)

            metadataSum = 0
            if not n:
                # get all metadata entries
                for j in range(i, i+m):
                    metadataSum += self.ins[j]
            else:
                # get metadata entries from children
                for j in range(i, i+m):
                    k = self.ins[j]
                    if 0 < k <= n:
                        metadataSum += childMetadata[k-1]

            return (i+m, metadataSum)
        (_, metadataSum) = postorder()
        print("Sum of all metadata entries:", metadataSum)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
