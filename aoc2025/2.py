QUIZ_NUMBER = "2"


class Solution:
    def run(fileName=QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, "r")
        arr = list(map(str, fp.read().split("\n")))
        for i in range(0, len(arr)):
            line = arr[i].split(",")
            for id_range in line:
                ids = id_range.split("-")
                if len(ids) == 2:
                    self.ins.append(list(map(int, ids)))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        sum_invalid = 0
        for first, last in self.ins:
            for i in range(first, last + 1):
                id_str = str(i)
                if len(id_str) % 2:
                    continue
                is_repeated = False
                s = len(id_str) // 2
                j = 0
                if id_str[j : j + s] == id_str[j + s : j + s * 2]:
                    sum_invalid += i
                    # print(f"Found invalid: {i} of {first}-{last}")
        print(f"Sum of invalid IDs: {sum_invalid}")

    def solve2(self):
        print("--- Part Two ---")
        sum_invalid = 0
        for first, last in self.ins:
            for i in range(first, last + 1):
                id_str = str(i)
                for s in range(1, len(id_str)):
                    if len(id_str) % s:
                        continue
                    is_repeated = True
                    j = 0
                    while j + s * 2 - 1 < len(id_str):
                        if id_str[j : j + s] != id_str[j + s : j + s * 2]:
                            is_repeated = False
                            break
                        j += s
                    if is_repeated:
                        sum_invalid += i
                        break
        print(f"Sum of invalid IDs: {sum_invalid}")


def main():
    Solution.test()
    Solution.run()


if __name__ == "__main__":
    main()
