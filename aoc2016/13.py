QUIZ_NUMBER = "13"

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
        xn, yn = 50, 50
        # xt, yt = 7, 4
        xt, yt = 31, 39
        maze = [['.' for x in range(xn)] for y in range(yn)]

        # fill the maze
        for x in range(xn):
            for y in range(yn):
                isWall = False
                yoyoma = x*x + 3*x + 2*x*y + y + y*y + self.ins
                while yoyoma:
                    yoyoma &= yoyoma-1
                    isWall = not isWall
                if isWall:
                    maze[y][x] = '#'

        # bfs to get shortest path
        q = [(1,1)] # y,x
        seen = set()
        steps = 0
        while q:
            qn = len(q)
            while qn:
                qn -= 1
                (y,x) = q.pop(0)
                seen.add((y,x))
                if y == yt and x == xt:
                    print(f"Fewest number of steps required to reach {xt},{yt}: {steps}")
                    return
                ny,nx = y,x-1
                if nx >= 0 and (ny,nx) not in seen and maze[ny][nx] == '.':
                    seen.add((ny,nx))
                    q.append((ny,nx))
                ny,nx = y,x+1
                if nx < xn and (ny,nx) not in seen and maze[ny][nx] == '.':
                    seen.add((ny,nx))
                    q.append((ny,nx))
                ny,nx = y-1,x
                if ny >= 0 and (ny,nx) not in seen and maze[ny][nx] == '.':
                    seen.add((ny,nx))
                    q.append((ny,nx))
                ny,nx = y+1,x
                if ny < yn and (ny,nx) not in seen and maze[ny][nx] == '.':
                    seen.add((ny,nx))
                    q.append((ny,nx))
            steps += 1

    def solve2(self):
        print("--- Part Two ---")
        xn, yn = 50, 50
        # xt, yt = 7, 4
        xt, yt = 31, 39
        maze = [['.' for x in range(xn)] for y in range(yn)]

        # fill the maze
        for x in range(xn):
            for y in range(yn):
                isWall = False
                yoyoma = x*x + 3*x + 2*x*y + y + y*y + self.ins
                while yoyoma:
                    yoyoma &= yoyoma-1
                    isWall = not isWall
                if isWall:
                    maze[y][x] = '#'

        # bfs to get shortest path
        q = [(1,1)] # y,x
        seen = set()
        steps = 51
        while steps:
            qn = len(q)
            while qn:
                qn -= 1
                (y,x) = q.pop(0)
                seen.add((y,x))
                ny,nx = y,x-1
                if nx >= 0 and (ny,nx) not in seen and maze[ny][nx] == '.':
                    q.append((ny,nx))
                ny,nx = y,x+1
                if nx < xn and (ny,nx) not in seen and maze[ny][nx] == '.':
                    q.append((ny,nx))
                ny,nx = y-1,x
                if ny >= 0 and (ny,nx) not in seen and maze[ny][nx] == '.':
                    q.append((ny,nx))
                ny,nx = y+1,x
                if ny < yn and (ny,nx) not in seen and maze[ny][nx] == '.':
                    q.append((ny,nx))
            steps -= 1
        print(f"Number of locations that can be reached in 50 steps: {len(seen)}")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
