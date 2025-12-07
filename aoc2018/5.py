QUIZ_NUMBER = "5"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.createMapping()
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

    def createMapping(self):
        def addMapEntry(mapping, a, A):
            mapping[a] = A
            mapping[A] = a
        self.mapping = dict()
        addMapEntry(self.mapping, 'a', 'A')
        addMapEntry(self.mapping, 'b', 'B')
        addMapEntry(self.mapping, 'c', 'C')
        addMapEntry(self.mapping, 'd', 'D')
        addMapEntry(self.mapping, 'e', 'E')
        addMapEntry(self.mapping, 'f', 'F')
        addMapEntry(self.mapping, 'g', 'G')
        addMapEntry(self.mapping, 'h', 'H')
        addMapEntry(self.mapping, 'i', 'I')
        addMapEntry(self.mapping, 'j', 'J')
        addMapEntry(self.mapping, 'k', 'K')
        addMapEntry(self.mapping, 'l', 'L')
        addMapEntry(self.mapping, 'm', 'M')
        addMapEntry(self.mapping, 'n', 'N')
        addMapEntry(self.mapping, 'o', 'O')
        addMapEntry(self.mapping, 'p', 'P')
        addMapEntry(self.mapping, 'q', 'Q')
        addMapEntry(self.mapping, 'r', 'R')
        addMapEntry(self.mapping, 's', 'S')
        addMapEntry(self.mapping, 't', 'T')
        addMapEntry(self.mapping, 'u', 'U')
        addMapEntry(self.mapping, 'v', 'V')
        addMapEntry(self.mapping, 'w', 'W')
        addMapEntry(self.mapping, 'x', 'X')
        addMapEntry(self.mapping, 'y', 'Y')
        addMapEntry(self.mapping, 'z', 'Z')

    def solve1(self, bans = ""):
        if not bans:
            print("--- Part One ---")
        stack = []
        for c in self.ins:
            if not stack:
                stack.append(c)
            elif c not in bans and self.mapping[stack[-1]] == c:
                stack.pop()
            elif c not in bans:
                stack.append(c)
        # print("Remaining polymer:", "".join(stack))
        if not bans:
            print("Units remaining after fully reacting the polymer:", len(stack))
        else:
            print("Units remaining after removing", bans, "then fully reacting the polymer:", len(stack))
        return len(stack)

    def solve2(self):
        print("--- Part Two ---")
        polymerTypes = [
            "aA",
            "bB",
            "cC",
            "dD",
            "eE",
            "fF",
            "gG",
            "hH",
            "iI",
            "jJ",
            "kK",
            "lL",
            "mM",
            "oO",
            "pP",
            "qQ",
            "rR",
            "sS",
            "tT",
            "uU",
            "vV",
            "wW",
            "xX",
            "yY",
            "zZ"
        ]

        shortestPolymer = len(self.ins)
        for type in polymerTypes:
            shortestPolymer = min(shortestPolymer, self.solve1(type))
        print("Shortest polymer possible:", shortestPolymer)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
