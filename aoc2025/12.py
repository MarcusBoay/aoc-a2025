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
        self.shapes = []
        self.sizes = []
        self.presents = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))

        is_shape = False
        shape = []
        for i in range(0, len(arr)-1):
            # print(arr[i])
            if not is_shape and arr[i][-1] == ':':
                is_shape = True
                continue
            if is_shape:
                if len(arr[i]):
                    shape.append(list(arr[i][::]))
                else:
                    is_shape = False
                    self.shapes.append(shape[::])
                    shape = []
            else:
                line = arr[i].split()
                self.sizes.append(line[0][0:-1].split('x'))
                self.presents.append(line[1::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total_regions = 0
        for i in range(len(self.presents)):
            size = self.sizes[i]
            presents = self.presents[i]

            shape_units = 0
            for j in range(len(presents)):
                p = int(presents[j])
                raw_shape = self.shapes[j]
                cur_shape_units = 0
                for si in range(len(raw_shape)):
                    for sj in range(len(raw_shape[si])):
                        c = raw_shape[si][sj]
                        if c == '#':
                            cur_shape_units += 1
                cur_shape_units *= p
                shape_units += cur_shape_units

            if shape_units < int(size[0]) * int(size[1]):
                total_regions += 1

        print(f"Total regions: {total_regions}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
