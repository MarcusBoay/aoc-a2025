QUIZ_NUMBER = "3"

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
            line = list(map(int, list(arr[i])))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total_output = 0
        for bank in self.ins:
            largest = 0
            for i in range(len(bank)):
                for j in range(i):
                    if i == j:
                        continue
                    largest = max(largest, bank[j]*10 + bank[i])

            total_output += largest
        print(f"Total output joltage: {total_output}")

    def solve2(self):
        print("--- Part Two ---")
        total_output = 0
        for bank in self.ins:
            largest_joltage = 0
            n = 0
            i = -1
            while (n < 12):
                # multiple previous result by 10
                largest_joltage *= 10
                # greedily choose the biggest number from the previously taken index
                # choose the first biggest number
                num = 0
                for j in range(i+1, len(bank)-(12-n-1)):
                    if num < bank[j]:
                        i = j 
                        num = bank[j]
                largest_joltage += num
                n += 1

            total_output += largest_joltage
        print(f"Total output joltage: {total_output}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
