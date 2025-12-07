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
        for i in range(0, len(arr)-1):
            line = list(arr[i])
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        times_split = 0
        q = []

        # find S
        for j in range(len(self.ins[0])):
            if self.ins[0][j] == 'S':
                q.append((0,j))
                self.start = (0,j)
                break

        # start splitting
        is_out_of_bounds = False
        seen = set()
        while not is_out_of_bounds:
            qn = len(q)
            while qn:
                qn -= 1
                cur = q.pop(0)

                if cur[0] >= len(self.ins):
                    is_out_of_bounds = True
                    break
 
                next = [(cur[0]+1, cur[1])]
                if next[0][0] >= len(self.ins):
                    is_out_of_bounds = True
                    break
                if next[0] in seen:
                    continue

                if self.ins[next[0][0]][next[0][1]] == '^':
                    times_split += 1
                    l = (next[0][0], next[0][1]-1)
                    r = (next[0][0], next[0][1]+1)
                    next = [l, r]

                for n in next:
                    if n not in seen:
                        q.append(n)
                        seen.add(n)
        print(f"Times split: {times_split}")


    def solve2(self):
        print("--- Part Two ---")
        self.timelines = 0

        q = [(self.start[0], self.start[1])]
        is_out_of_bounds = False
        seen = dict()
        seen[q[0]] = 1
        while q:
            qn = len(q)
            while qn:
                qn -= 1
                cur = q.pop(0)

                # if cur[0] >= len(self.ins):
                #     self.timelines += seen[cur]
                #     continue
                next = [(cur[0]+1, cur[1])]
                if next[0][0] >= len(self.ins):
                    self.timelines += seen[cur]
                    continue
                if self.ins[next[0][0]][next[0][1]] == '^':
                    l = (next[0][0], next[0][1]-1)
                    r = (next[0][0], next[0][1]+1)
                    next = [l, r]
                for n in next:
                    if n not in seen:
                        seen[n] = seen[cur]
                        q.append(n)
                    else:
                        seen[n] += seen[cur]

        print(f"Total timelines: {self.timelines}")


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
