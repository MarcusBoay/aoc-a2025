QUIZ_NUMBER = "11"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve(self):
        print("--- Part One ---")
        pn = 0
        first = [True] * 8
        for ai in range(ord(self.ins[0]), ord('z')+1):
            bs = ord(self.ins[1]) if first[1] else ord('a')
            first[1] = False
            for bi in range(bs, ord('z')+1):
                cs = ord(self.ins[2]) if first[2] else ord('a')
                first[2] = False
                for ci in range(cs, ord('z')+1):
                    ds = ord(self.ins[3]) if first[3] else ord('a')
                    first[3] = False
                    for di in range(ds, ord('z')+1):
                        es = ord(self.ins[4]) if first[4] else ord('a')
                        first[4] = False
                        for ei in range(es, ord('z')+1):
                            fs = ord(self.ins[5]) if first[5] else ord('a')
                            first[5] = False
                            for fi in range(fs, ord('z')+1):
                                gs = ord(self.ins[6]) if first[6] else ord('a')
                                first[6] = False
                                for gi in range(gs, ord('z')+1):
                                    hs = ord(self.ins[7])+1 if first[7] else ord('a')
                                    first[7] = False
                                    for hi in range(hs, ord('z')+1):
                                        a, b, c, d, e, f, g, h = \
                                            chr(ai), chr(bi), chr(ci), chr(di), \
                                            chr(ei), chr(fi), chr(gi), chr(hi)
                                        hasIncreasingStraight = \
                                            ord(a) == ord(b)-1 == ord(c)-2 or \
                                            ord(b) == ord(c)-1 == ord(d)-2 or \
                                            ord(c) == ord(d)-1 == ord(e)-2 or \
                                            ord(d) == ord(e)-1 == ord(f)-2 or \
                                            ord(e) == ord(f)-1 == ord(g)-2 or \
                                            ord(f) == ord(g)-1 == ord(h)-2
                                        containsIOL = \
                                            a in "iol" or \
                                            b in "iol" or \
                                            c in "iol" or \
                                            d in "iol" or \
                                            e in "iol" or \
                                            f in "iol" or \
                                            g in "iol" or \
                                            h in "iol"
                                        p = a + b + c + d + e + f + g + h
                                        pairs = 0
                                        pi = 0
                                        while pi < 7:
                                            if p[pi] == p[pi+1]:
                                                pairs += 1
                                                pi += 1
                                            pi += 1
                                        if hasIncreasingStraight and \
                                           not containsIOL and \
                                           pairs >= 2:
                                            print("Next password:", p)
                                            pn += 1
                                            if pn >= 2:
                                                return

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
