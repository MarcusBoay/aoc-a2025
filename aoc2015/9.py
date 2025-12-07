QUIZ_NUMBER = "9"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            self.ins.append([line[0], line[2], int(line[4])])
        fp.close()
        print("===", self.fileName, "===")

    def solve(self):
        print("--- Part One ---")
        # get mapping of name to ID
        idMap = dict()
        i = 0
        for route in self.ins:
            if route[0] not in idMap:
                idMap[route[0]] = i
                i += 1
            if route[1] not in idMap:
                idMap[route[1]] = i
                i += 1
        n = i

        # adjacency matrix
        v = [[None for j in range(n)] for k in range(n)]
        for route in self.ins:
            n1, n2 = idMap[route[0]], idMap[route[1]]
            v[n1][n2], v[n2][n1] = route[2], route[2]

        self.shortestPath = None
        self.longestPath = None

        def backtrack(seen, path, i, n):
            if len(seen) == n:
                if not self.shortestPath:
                    self.shortestPath = path
                if not self.longestPath:
                    self.longestPath = path
                self.shortestPath = min(self.shortestPath, path)
                self.longestPath = max(self.longestPath, path)
                return

            for j in range(n):
                if i != j and v[i][j] and j not in seen:
                    seen.add(j)
                    backtrack(seen.copy(), path+v[i][j], j, n)
                    seen.remove(j)

        for i in range(n):
            seen = set()
            seen.add(i)
            backtrack(seen, 0, i, n)
        print("Shortest route:", self.shortestPath)
        # TODO
        # challenge: implement part one using BFS instead
        # challeng : implement using academia pseudocode
        print("--- Part Two ---")
        print("Longest path:", self.longestPath)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
