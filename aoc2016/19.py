QUIZ_NUMBER = "19"

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
        self.ins = int(fp.read())
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        twoN = 1
        r = self.ins
        while r:
            r >>= 1
            twoN <<= 1
        twoN >>= 1
        r = self.ins - twoN
        winningElf = (r << 1) + 1
        print(f"Elf that gets all the presents: {winningElf}")

    def solve2(self):
        print("--- Part Two ---")
        # for n in range(2, 210):
        #     arr = [0] * n
        #     for i in range(n):
        #         arr[i] = i+1
        #     while len(arr) > 1:
        #         arr.pop(len(arr)//2)
        #         prev = arr.pop(0)
        #         arr.append(prev)
        #     print(f"{n}: {arr[0]}")
        # it seems be powers of 3 in this case, and after the reset, it increases by 1 until it equals the previous power of 3 then it increases by 2 until the next power of 3 where it caps at itself
        r = self.ins
        threeN = -1
        while r >= 3:
            r //= 3
            threeN += 1
        rem = 0
        t = 3
        while threeN:
            t *= 3
            threeN -= 1
        rem = self.ins - t
        # print(rem)
        if rem <= t:
            winningElf = rem
        else:
            rem -= t
            rem *= 2
            winningElf = t + rem
        print(f"Elf that gets all the presents: {winningElf}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
