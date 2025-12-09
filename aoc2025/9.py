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
        for t1 in self.ins:
            for t2 in self.ins:
                dx, dy = abs(t1[0]-t2[0])+1, abs(t1[1]-t2[1])+1
                area = dx * dy
                largest_area = max(area, largest_area)
        print(f"Largest area: {largest_area}")

    def crossProduct(self, v1, v2):
        return v1[0]*v2[1]*1.0 - v1[1]*v2[0]*1.0

    def diff(self, v1, v2):
        return [v2[0]-v1[0], v2[1]-v1[1]]

    def sum(self, v1, v2):
        return [v1[0]+v2[0], v1[1]+v2[1]]

    def solve2(self):
        print("--- Part Two ---")
        # holds direction vector of every point
        directions = []
        c = 0
        while c < len(self.ins):
            v1, v2 = self.ins[c-1], self.ins[c]
            directions.append(self.diff(v1, v2))
            c += 1

        # if intersection_point is any one of the vertices, rect is in the green zone
        largest_area = 1
        for ai in range(len(self.ins)):
            for bi in range(len(self.ins)):
                if ai == bi:
                    continue
                a, b = self.ins[ai][::], self.ins[bi][::]
                d1 = self.diff(a, b)
                is_intersecting = False
                for d2i in range(len(self.ins)):
                    c, d = self.ins[d2i-1], self.ins[d2i]
                    d2 = directions[d2i]
                    divisor = (self.crossProduct(d1, d2)*1.0)
                    if divisor == 0:
                        continue
                    t1 = self.crossProduct(self.diff(a, c), d2) / divisor
                    d3 = [d1[0] * t1, d1[1] * t1]
                    intersection_point = self.sum(a, d3)
                    if intersection_point in [a,b,c,d]:
                        continue
                    else:
                        # check if intersection point is on the actual line ...
                        if c[0] <= d[0] and c[1] <= d[1] and \
                            c[0] <= intersection_point[0] <= d[0] and \
                            c[1] <= intersection_point[1] <= d[1]:
                            is_intersecting = True
                            break
                        if c[0] <= d[0] and c[1] >= d[1] and \
                            c[0] <= intersection_point[0] <= d[0] and \
                            d[1] <= intersection_point[1] <= c[1]:
                            is_intersecting = True
                            break
                        if c[0] >= d[0] and c[1] >= d[1] and \
                            d[0] <= intersection_point[0] <= c[0] and \
                            d[1] <= intersection_point[1] <= c[1]:
                            is_intersecting = True
                            break
                        if c[0] >= d[0] and c[1] <= d[1] and \
                            d[0] <= intersection_point[0] <= c[0] and \
                            c[1] <= intersection_point[1] <= d[1]:
                            is_intersecting = True
                            break
                if not is_intersecting:
                    a, b = [a[0], b[1]], [a[1], b[0]]
                    d1 = self.diff(a, b)
                    is_intersecting = False
                    for d2i in range(len(self.ins)):
                        c, d = self.ins[d2i-1], self.ins[d2i]
                        d2 = directions[d2i]
                        divisor = (self.crossProduct(d1, d2)*1.0)
                        if divisor == 0:
                            continue
                        t1 = self.crossProduct(self.diff(a, c), d2) / divisor
                        d3 = [d1[0] * t1, d1[1] * t1]
                        intersection_point = self.sum(a, d3)
                        if intersection_point in [a,b,c,d]:
                            continue
                        else:
                            # check if intersection point is on the actual line ...
                            if c[0] <= d[0] and c[1] <= d[1] and \
                                c[0] <= intersection_point[0] <= d[0] and \
                                c[1] <= intersection_point[1] <= d[1]:
                                is_intersecting = True
                                break
                            if c[0] <= d[0] and c[1] >= d[1] and \
                                c[0] <= intersection_point[0] <= d[0] and \
                                d[1] <= intersection_point[1] <= c[1]:
                                is_intersecting = True
                                break
                            if c[0] >= d[0] and c[1] >= d[1] and \
                                d[0] <= intersection_point[0] <= c[0] and \
                                d[1] <= intersection_point[1] <= c[1]:
                                is_intersecting = True
                                break
                            if c[0] >= d[0] and c[1] <= d[1] and \
                                d[0] <= intersection_point[0] <= c[0] and \
                                c[1] <= intersection_point[1] <= d[1]:
                                is_intersecting = True
                                break
                    if not is_intersecting:
                        a, b = self.ins[ai], self.ins[bi]
                        d1 = self.diff(a, b)
                        area = (abs(d1[0])+1) * (abs(d1[1]+1))
                        largest_area = max(largest_area, area)
                        print(area, a, b)
        print(f"Largest area: {largest_area}")



def main():
    Solution.test()
    # Solution.run()

if __name__ == "__main__":
    main()
