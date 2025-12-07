QUIZ_NUMBER = "12"

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
            line = arr[i].split(" <-> ")
            line[1] = line[1].split(", ")
            self.ins.append(line[:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        q = ["0"]
        seen = set()
        while q:
            qn = len(q)
            while qn:
                cur = q.pop(0)
                qn -= 1
                seen.add(cur)
                for next in self.ins[int(cur)][1]:
                    if next not in seen:
                        seen.add(next)
                        q.append(next)
        print(f"Number of programs that contain the program ID 0: {len(seen)}")

    def solve2(self):
        print("--- Part Two ---")
        groups = 0
        seen = set()
        for i in range(len(self.ins)):
            if str(i) not in seen:
                q = [i]
                while q:
                    qn = len(q)
                    while qn:
                        cur = q.pop(0)
                        qn -= 1
                        seen.add(cur)
                        for next in self.ins[int(cur)][1]:
                            if next not in seen:
                                seen.add(next)
                                q.append(next)
                groups += 1
        print(f"Number of groups: {groups}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
