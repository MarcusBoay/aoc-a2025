QUIZ_NUMBER = "10"
import math

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        # solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")
        self.n = 50

    def solve1(self):
        print("--- Part One ---")
        sequence = list(map(str, self.ins[::]))
        n = self.n
        for _ in range(n):
            curDigit = None
            quantity = 0
            nextSequence = []
            while sequence:
                if not curDigit:
                    curDigit = sequence.pop(0)
                    quantity = 1
                    continue
                nextDigit = sequence.pop(0)
                if curDigit == nextDigit:
                    quantity += 1
                else:
                    nextSequence.append(str(quantity))
                    nextSequence.append(curDigit)
                    curDigit = nextDigit
                    quantity = 1
            nextSequence.append(str(quantity))
            nextSequence.append(curDigit)
            sequence = nextSequence[::]
        print("Length of result after", n, "iterations:", len(sequence))
        self.p1ans = len(sequence)

    def solve2(self):
        print("--- Part Two ---")
        elements = [
            0, # N/A
            22, # 1
            13112221133211322112211213322112, # 2
            312211322212221121123222112, # 3
            111312211312113221133211322112211213322112, # 4
            1321132122211322212221121123222112, # 5
            3113112211322112211213322112, # 6
            111312212221121123222112, # 7
            132112211213322112, # 8
            31121123222112, # 9
            111213322112, # 10
            123222112, # 11
            3113322112, # 12
            1113222112, # 13
            1322112, # 14
            311311222112, # 15
            1113122112, # 16
            132112, # 17
            3112, # 18
            1112, # 19
            12, # 20
            3113112221133112, # 21
            11131221131112, # 22
            13211312, # 23
            31132, # 24
            111311222112, # 25
            13122112, # 26
            32112, # 27
            11133112, # 28
            131112, # 29
            312, # 30
            13221133122211332, # 31
            31131122211311122113222, # 32
            11131221131211322113322112, # 33
            13211321222113222112, # 34
            3113112211322112, # 35
            11131221222112, # 36
            1321122112, # 37
            3112112, # 38
            1112133, # 39
            12322211331222113112211, # 40
            1113122113322113111221131221, # 41
            13211322211312113211, # 42
            311322113212221, # 43
            132211331222113112211, # 44
            311311222113111221131221, # 45
            111312211312113211, # 46
            132113212221, # 47
            3113112211, # 48
            11131221, # 49
            13211, # 50
            3112221, # 51
            1322113312211, # 52
            311311222113111221, # 53
            11131221131211, # 54
            13211321, # 55
            311311, # 56
            11131, # 57
            1321133112, # 58
            31131112, #59
            111312, # 60
            132, # 61
            311332, # 62
            1113222, # 63
            13221133112, # 64
            3113112221131112, # 65
            111312211312, # 66
            1321132, # 67
            311311222, # 68
            11131221133112, # 69
            1321131112, # 70
            311312, # 71
            11132, # 72
            13112221133211322112211213322113, # 73
            312211322212221121123222113, # 74
            111312211312113221133211322112211213322113, # 75
            1321132122211322212221121123222113, # 76
            3113112211322112211213322113, # 77
            111312212221121123222113, # 78
            132112211213322113, # 79
            31121123222113, # 80
            111213322113, # 81
            123222113, # 82
            3113322113, # 83
            1113222113, # 84
            1322113, # 85
            311311222113, # 86
            1113122113, # 87
            132113, # 88
            3113, # 89
            1113, # 90
            13, # 91
            3, # 92
        ]
        decaysInto = dict()
        decaysInto[1] = [1]
        decaysInto[2] = [72, 91, 1, 20, 3]
        decaysInto[3] = [2]
        decaysInto[4] = [32, 20, 3]
        decaysInto[5] = [4]
        decaysInto[6] = [5]
        decaysInto[7] = [6]
        decaysInto[8] = [7]
        decaysInto[9] = [8]
        decaysInto[10] = [9]
        decaysInto[11] = [10]
        decaysInto[12] = [61, 11]
        decaysInto[13] = [12]
        decaysInto[14] = [13]
        decaysInto[15] = [67, 14]
        decaysInto[16] = [15]
        decaysInto[17] = [16]
        decaysInto[18] = [17]
        decaysInto[19] = [18]
        decaysInto[20] = [19]
        decaysInto[21] = [67, 91, 1, 20, 27]
        decaysInto[22] = [21]
        decaysInto[23] = [22]
        decaysInto[24] = [23]
        decaysInto[25] = [24, 14]
        decaysInto[26] = [25]
        decaysInto[27] = [26]
        decaysInto[28] = [30, 27]
        decaysInto[29] = [28]
        decaysInto[30] = [29]
        decaysInto[31] = [63, 20, 89, 1, 20, 30]
        decaysInto[32] = [67, 31]
        decaysInto[33] = [32, 11]
        decaysInto[34] = [33]
        decaysInto[35] = [34]
        decaysInto[36] = [35]
        decaysInto[37] = [36]
        decaysInto[38] = [37]
        decaysInto[39] = [38, 92]
        decaysInto[40] = [39, 1, 20, 43]
        decaysInto[41] = [68, 40]
        decaysInto[42] = [41]
        decaysInto[43] = [42]
        decaysInto[44] = [63, 20, 43]
        decaysInto[45] = [67, 44]
        decaysInto[46] = [45]
        decaysInto[47] = [46]
        decaysInto[48] = [47]
        decaysInto[49] = [48]
        decaysInto[50] = [49]
        decaysInto[51] = [61, 50]
        decaysInto[52] = [63, 20, 51]
        decaysInto[53] = [67, 52]
        decaysInto[54] = [53]
        decaysInto[55] = [54]
        decaysInto[56] = [55]
        decaysInto[57] = [56]
        decaysInto[58] = [57, 1, 20, 27]
        decaysInto[59] = [58]
        decaysInto[60] = [59]
        decaysInto[61] = [60]
        decaysInto[62] = [61, 20, 30]
        decaysInto[63] = [62]
        decaysInto[64] = [63, 20, 27]
        decaysInto[65] = [67, 64]
        decaysInto[66] = [65]
        decaysInto[67] = [66]
        decaysInto[68] = [67, 61]
        decaysInto[69] = [68, 20, 27]
        decaysInto[70] = [69]
        decaysInto[71] = [70]
        decaysInto[72] = [71]
        decaysInto[73] = [72, 91, 1, 20, 74]
        decaysInto[74] = [73]
        decaysInto[75] = [32, 20, 74]
        decaysInto[76] = [75]
        decaysInto[77] = [76]
        decaysInto[78] = [77]
        decaysInto[79] = [78]
        decaysInto[80] = [79]
        decaysInto[81] = [80]
        decaysInto[82] = [81]
        decaysInto[83] = [61, 82]
        decaysInto[84] = [83]
        decaysInto[85] = [84]
        decaysInto[86] = [67, 85]
        decaysInto[87] = [86]
        decaysInto[88] = [87]
        decaysInto[89] = [88]
        decaysInto[90] = [89]
        decaysInto[91] = [90]
        decaysInto[92] = [91]

        s = 0
        for i in range(len(elements)):
            if self.ins == str(elements[i]):
                s = i
                break
        if not s:
            print("Cannot find starting element with sequence:", self.ins)
            print("Aborting...")
            return

        q = [s]
        curIte = 0
        n = self.n
        while curIte < n:
            curIte += 1
            qn = len(q)
            if curIte > 40:
                print("iteration", curIte)
            while qn:
                e = q.pop(0)
                qn -= 1
                decayed = decaysInto[e]
                for d in decayed:
                    q.append(d)

        totalLength = 0
        for e in q:
            totalLength += len(str(elements[e]))
        print("Total length after", n,"iterations:", totalLength)


def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
