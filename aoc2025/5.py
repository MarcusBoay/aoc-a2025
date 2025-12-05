QUIZ_NUMBER = "5"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.fileName = fileName
        self.id_ranges = []
        self.ids = []
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))

        is_id_range = True
        for i in range(0, len(arr)-1):
            if len(arr[i]) == 0:
                is_id_range = False
                continue

            if is_id_range:
                line = list(map(int, arr[i].split('-')))
                self.id_ranges.append(line[::])
            else:
                self.ids.append(int(arr[i]))

        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total_fresh = 0
        for id in self.ids:
            is_fresh = False
            for start, end in self.id_ranges:
                if start <= id and id <= end:
                    is_fresh = True
                    break
            if is_fresh:
                total_fresh += 1
        print(f"Total fresh ingredients: {total_fresh}")

    def solve2(self):
        print("--- Part Two ---")
        sorted_ids = sorted(self.id_ranges, key=lambda x: x[0])
        merged = []
        for sn, en in sorted_ids:
            if not merged:
                merged.append([sn, en])
                continue
            s, e = merged[-1][0], merged[-1][1]
            if sn <= e and en > e:
                merged[-1][1] = en
            elif sn > e:
                merged.append([sn, en])
        total_fresh = 0
        for s, e in merged:
            total_fresh += e - s + 1
        print(f"Total fresh ingredients: {total_fresh}")


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
