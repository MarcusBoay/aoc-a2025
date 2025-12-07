QUIZ_NUMBER = "5"

# seed-to-soil map:
# 50 98 2
# 52 50 48
# destination range start, source range start, range length
# sources: 98 99, destinations: 50, 51
# seed 98 goes to 50, seed 99 goes to 51
# Any source numbers that aren't mapped correspond to the same destination number.
# So, seed number 10 corresponds to soil number 10.
class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        lines = []
        self.ins.append(list(map(int, arr[0].split())))
        for i in range(2, len(arr)):
            if len(arr[i]):
                lines.append(list(map(int, arr[i].split())))
            else:
                self.ins.append(lines[::])
                lines = []
        fp.close()

        # self.ins[0] is seeds
        # self.ins[1] is seed-to-soil map
        # self.ins[2] is soil-to-fertilizer map
        # self.ins[3] is fertilizer-to-water map
        # self.ins[4] is water-to-light map
        # self.ins[5] is light-to-temperature map
        # self.ins[6] is temperature-to-humidity map
        # self.ins[7] is humidity-to-location map
        # for i in range(len(self.ins)):
        #     print(self.ins[i])

    def solve1(self):
        print("--- Part One ---")
        locations = []
        for seed in self.ins[0]:
            print("seed", seed)
            start = seed
            next = seed
            for i in range(1, len(self.ins)):
                start = next
                found = False
                # iterate over start-to-end map
                curMap = self.ins[i]
                for e in curMap:
                    if e[1] <= start < (e[1] + e[2]):
                        found = True
                        diff = start - e[1]
                        next = e[0] + diff
                        break

                if not found:
                    next = start
                print("mapping", i, "->", next)
            locations.append(next)
        print("Lowest location:", min(locations))

    def solve2(self):
        print("--- Part Two ---")
        minLocation = 278755257 # some large number...
        seed_location_map = dict()
        for p in range(0, len(self.ins[0]), 2):
            seed_range_start = self.ins[0][p]
            seed_range_length = self.ins[0][p+1]
            for seed in range(seed_range_start, seed_range_start + seed_range_length):
                if seed in seed_location_map:
                    break
                start = seed
                next = seed
                for i in range(1, len(self.ins)):
                    start = next
                    found = False
                    # iterate over start-to-end map
                    curMap = self.ins[i]
                    for e in curMap:
                        if e[1] <= start < (e[1] + e[2]):
                            found = True
                            diff = start - e[1]
                            next = e[0] + diff
                            break

                    if not found:
                        next = start
                    # print("mapping", i, "->", next)
                seed_location_map[seed] = next
                minLocation = min(minLocation, next)
        print("Lowest location:", minLocation)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
