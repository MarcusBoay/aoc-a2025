import hashlib


QUIZ_NUMBER = "17"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.fileName = fileName
        fp = open(fileName, 'r')
        self.ins = fp.read()
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        q = [(0,0,self.ins)]
        longestPath = 0
        while q:
            qn = len(q)
            while qn:
                qn -= 1
                i,j,p = q.pop(0)
                if i == 3 and j == 3:
                    print(f"Shortest path: {p[len(self.ins)::]}")
                    return
                m = hashlib.md5()
                m.update(p.encode())
                h = m.hexdigest()
                ni,nj = i-1,j
                if ni >= 0 and h[0] in "bcdef":
                    q.append((ni,nj,p+'U'))
                ni,nj = i+1,j
                if ni < 4 and h[1] in "bcdef":
                    q.append((ni,nj,p+'D'))
                ni,nj = i,j-1
                if nj >= 0 and h[2] in "bcdef":
                    q.append((ni,nj,p+'L'))
                ni,nj = i,j+1
                if nj < 4 and h[3] in "bcdef":
                    q.append((ni,nj,p+'R'))

    def solve2(self):
        print("--- Part Two ---")
        q = [(0,0,self.ins)]
        maxSteps = 0
        curSteps = 0
        while q:
            qn = len(q)
            while qn:
                qn -= 1
                i,j,p = q.pop(0)
                if i == 3 and j == 3:
                    maxSteps = max(maxSteps, curSteps)
                    continue
                    # return
                m = hashlib.md5()
                m.update(p.encode())
                h = m.hexdigest()
                ni,nj = i-1,j
                if ni >= 0 and h[0] in "bcdef":
                    q.append((ni,nj,p+'U'))
                ni,nj = i+1,j
                if ni < 4 and h[1] in "bcdef":
                    q.append((ni,nj,p+'D'))
                ni,nj = i,j-1
                if nj >= 0 and h[2] in "bcdef":
                    q.append((ni,nj,p+'L'))
                ni,nj = i,j+1
                if nj < 4 and h[3] in "bcdef":
                    q.append((ni,nj,p+'R'))
            curSteps += 1
        print(f"Longest path that reaches the vault: {maxSteps}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
