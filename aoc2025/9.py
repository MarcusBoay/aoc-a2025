import matplotlib.pyplot as plt

QUIZ_NUMBER = "9"

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
            line = list(map(int ,arr[i].split(',')))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        largest_area = 0
        self.largest_areas = []
        for t1 in self.ins:
            for t2 in self.ins:
                dx, dy = abs(t1[0]-t2[0])+1, abs(t1[1]-t2[1])+1
                area = dx * dy
                largest_area = max(area, largest_area)
                self.largest_areas.append([area, t1, t2])
        print(f"Largest area: {largest_area}")

    def solve2(self):
        print("--- Part Two ---")

        # input
        x = []
        y = []
        for i in range(len(self.ins)):
            # if i > 249:
            #     break
            row = self.ins[i]
            x.append(row[0])
            y.append(row[1])
        x.append(self.ins[0][0])
        y.append(self.ins[0][1])

        # candidate
        # p1 = [17217, 85603]
        # p3 = [82570, 14626]
        # p1 = [84550,83468]
        # p3 = [16729,84345]
        fp = open("9.coords", 'r')
        arr = list(map(str, fp.read().split('\n')))
        areas_raw = []
        for row in arr:
            if not row:
                continue
            line = list(map(int, row.split(',')))
            areas_raw.append(line)
        fp.close()
        areas = sorted(areas_raw, key=lambda a : a[0])
        for ai in range(len(areas)-1, -1, -1):
            a = areas[ai]
            # if a[0] > 1500000000:
            #     continue
            p1, p3 = [a[1], a[2]], [a[3], a[4]]
            if (p1[0] < 50000 < p3[0] and p1[1] < 50000 < p3[1]) or \
                (p3[0] < 50000 < p1[0] and p3[1] < 50000 < p1[1]) or \
                (p1[0] < 50000 < p3[0] and p3[1] < 50000 < p1[1]) or \
                (p3[0] < 50000 < p1[0] and p1[1] < 50000 < p3[1]):
                continue
            print(a)
            px = [p1[0], p1[0], p3[0], p3[0], p1[0]]
            py = [p1[1], p3[1], p3[1], p1[1], p1[1]]
            plt.plot(x, y, 'b-', px, py, 'r--')#, [17217, 17217], [85603, 14626], 'g-', [9562, 9377], [74790, 74790], 'x-')
            plt.show()


def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
