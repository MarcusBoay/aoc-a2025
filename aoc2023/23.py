import sys
sys.setrecursionlimit(3000)

class ALongWalk:
    def test(fileName = "23.ex.in"):
        aLongWalk = ALongWalk(fileName)
        aLongWalk.solve1_backtrack()
        aLongWalk.solve2()

    def run():
        ALongWalk.test("23.in")

    def __init__(self, fileName):
        self.ins = []
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = [x for x in arr[i]]
            self.ins.append(line[::])
        fp.close()

    # def solve2_color(self):
    #     self.longestHike = 0
    #     self.
    #     # tiles currently hiking
    #     curTiles = [[0, 1]]
    #     # paths we can take; down, up, right, left
    #     actions = [[1,0],[-1,0],[0,-1],[0,1]]
    #     curStep = 0
    #     while queue:
    #         curStep += 1
    #         nextTiles = []

    #         # take one step to the next possible tiles from current tiles
    #         while queue:
    #             curTile = queue.pop(0)

    #             for action in actions:
    #                 nextPos = [i + action[0],
    #                            j + action[1]]

    #                 # boundary checking, make sure we're still on the map
    #                 if 0 <= nextPos[0] < len(self.ins) and \
    #                     0 <= nextPos[1] < len(self.ins[0]):
    #                     nextTile = self.ins[nextPos[0]][nextPos[1]]

    #                     # make sure that the next tile is possible to walk on
    #                     if nextTile in ".<v^>" or isinstance(nextTile, int):
    #                         nextTiles.append(nextPos[::])

    #         pass
    #     backtrack(0, 1)
    #     print("Longest hike:", self.longestHike)

    def solve1_backtrack(self):
        self.longestHike = 0
        def backtrack(i, j, step = 0):
            # base case, we've reached the end
            if i == len(self.ins)-1 and j == len(self.ins)-2:
                print("old longest hike:", self.longestHike, "cur hike:", step)
                self.longestHike = max(self.longestHike, step)

            # paths we can take; down, up, right, left
            for action in [[1,0],[-1,0],[0,-1],[0,1]]:
                ii, jj = i + action[0], j + action[1]

                # boundary checking, make sure we're still on the map
                if 0 <= ii < len(self.ins) and \
                    0 <= jj < len(self.ins[0]):
                    nextTile = self.ins[ii][jj]

                    # make sure that the next tile is possible to walk on
                    if nextTile == '.' or \
                       (action[0] == 1 and nextTile == 'v') or \
                       (action[0] == -1 and nextTile == '^') or \
                       (action[1] == 1 and nextTile == '>') or \
                       (action[1] == -1 and nextTile == '<'):
                        # walk to the next tile
                        self.ins[ii][jj] = 'O'
                        backtrack(ii, jj, step+1)
                        # ... come back to this tile
                        # revert marking of next tile
                        self.ins[ii][jj] = nextTile
        backtrack(0, 1)
        print("Longest hike:", self.longestHike)

    def solve2(self):
        pass

# ALongWalk.test()
ALongWalk.run()