QUIZ_NUMBER = "9"

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
        self.ins = list(map(int, fp.read().split()))
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        marbles = [0]
        players = self.ins[0]
        playerScores = [0] * players
        curPos = 0
        curPlayer = 0
        lastMarbleWorth = self.ins[1]
        # nextMarbles = [1]
        curMarble = 1

        while curMarble <= lastMarbleWorth+1:
            print(marbles)
            if len(marbles) == 20:
                marbles.insert(0, marbles.pop())
                curPos += 1
            curPos += 2
            curPos %= len(marbles)
            if curMarble % 23 != 0:
                marbles.insert(curPos, curMarble)
            else:
                # print(f"adding {curMarble} for player {curPlayer+1}")
                playerScores[curPlayer] += curMarble
                curPos -= 9
                removedMarble = marbles.pop(curPos%len(marbles))
                # print(f"adding removed marble {removedMarble} for player {curPlayer+1}")
                playerScores[curPlayer] += removedMarble
            curPlayer = (curPlayer+1)%players
            curMarble += 1
        # print(f"Player Scores: {playerScores}")
        # print(f"marbles: {marbles}")
        print(f"Winning Elf's score: {max(playerScores)}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    # Solution.run()

if __name__ == "__main__":
    main()
