QUIZ_NUMBER = "7"

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
            line = arr[i].split()
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

        # get hashmap of nodes (name: weight)
        self.nodes = dict()
        for row in self.ins:
            self.nodes[row[0]] = row[1]

    def solve1(self):
        print("--- Part One ---")

        # get all parents and childrens
        children = set()
        parents = set()
        for row in self.ins:
            if len(row) > 2:
                parents.add(row[0])
                i = 2
                while i < len(row):
                    children.add(row[i])
                    i += 1

        # remove all parents who are also children
        for child in children:
            if child in parents:
                parents.remove(child)

        print("Bottom program:", parents)

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
