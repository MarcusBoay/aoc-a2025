QUIZ_NUMBER = "19"

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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            self.ins.append(arr[i][:])
        fp.close()
        print("===", self.fileName, "===")

    def solve(self):
        direction = 'S'
        si, sj = 0, 0
        for j in range(len(self.ins[0])): # starting will always be from the top
            if self.ins[0][j] == '|':
                sj = j

        seen = set()
        seen.add((si, sj))
        q = [(si, sj)]
        letters = []
        steps = 0
        while q:
            (i, j) = q.pop(0)
            seen.add((i, j))
            if self.ins[i][j] == ' ':
                break
            steps += 1
            if self.ins[i][j].isalpha():
                letters.append(self.ins[i][j])
            # check cur location
            if self.ins[i][j] == '+':
                ni, nj = i-1, j
                if ni >= 0 and (ni, nj) not in seen and (self.ins[ni][nj] in "|-" or self.ins[ni][nj].isalpha()):
                    direction = 'N'
                ni, nj = i+1, j
                if ni < len(self.ins) and (ni, nj) not in seen and (self.ins[ni][nj] in "|-" or self.ins[ni][nj].isalpha()):
                    direction = 'S'
                ni, nj = i, j-1
                if nj >= 0 and (ni, nj) not in seen and (self.ins[ni][nj] in "|-" or self.ins[ni][nj].isalpha()):
                    direction = 'W'
                ni, nj = i, j+1
                if nj < len(self.ins[ni]) and (ni, nj) not in seen and (self.ins[ni][nj] in "|-" or self.ins[ni][nj].isalpha()):
                    direction = 'E'

            # move to next
            if direction == 'N':
                ni, nj = i-1, j
                q.append((ni, nj))
                seen.add((ni, nj))
            elif direction == 'S':
                ni, nj = i+1, j
                q.append((ni, nj))
                seen.add((ni, nj))
            elif direction == 'W':
                ni, nj = i, j-1
                q.append((ni, nj))
                seen.add((ni, nj))
            elif direction == 'E':
                ni, nj = i, j+1
                q.append((ni, nj))
                seen.add((ni, nj))

        print(f"Letters seen on the path: {"".join(letters)}")
        print(f"Number of steps to get to the end: {steps}")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
