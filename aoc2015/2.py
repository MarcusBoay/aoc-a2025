QUIZ_NUMBER = "2"

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
            line = list(map(int, arr[i].split()))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total = 0
        for dim in self.ins:
            l, w, h = dim[0], dim[1], dim[2]
            total += 2*l*w + 2*w*h + 2*h*l
            if l*w <= w*h and l*w <= h*l:
                total += l*w
            elif w*h <= l*w and w*h <= h*l:
                total += w*h
            elif h*l <= l*w and h*l <= w*h:
                total += h*l
        print("Total square feet of wrapping paper needed:", total)

    def solve2(self):
        print("--- Part Two ---")
        total = 0
        for dim in self.ins:
            l, w, h = dim[0], dim[1], dim[2]
            total += l*w*h
            p1, p2, p3 = 2*l + 2*w, 2*w + 2*h, 2*l + 2*h
            if p1 <= p2 and p1 <= p3:
                total += p1
            elif p2 <= p1 and p2 <= p3:
                total += p2
            elif p3 <= p1 and p3 <= p2:
                total += p3
        print("Total feet of ribbon needed:", total)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
