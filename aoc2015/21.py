QUIZ_NUMBER = "21"

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
        self.ins = list(map(int, fp.read().split(',')))
        fp.close()
        print("===", self.fileName, "===")
        self.weapons = dict()
        self.weapons["Dagger"] = (8, 4, 0) # cost, damage, armor
        self.weapons["Shortsword"] = (10, 5, 0)
        self.weapons["Warhammer"] = (25, 6, 0)
        self.weapons["Longsword"] = (40, 7, 0)
        self.weapons["Greataxe"] = (74, 8, 0)
        self.armor = dict()
        self.armor["Nothing"] = (0, 0, 0)
        self.armor["Leather"] = (13, 0, 1)
        self.armor["Chainmail"] = (31, 0, 2)
        self.armor["Splitmail"] = (53, 0, 3)
        self.armor["Bandedmail"] = (75, 0, 4)
        self.armor["Platemail"] = (102, 0, 5)
        self.rings = dict()
        self.rings["Nothing"] = (0, 0, 0)
        self.rings["Damage +1"] = (25, 1, 0)
        self.rings["Damage +2"] = (50, 2, 0)
        self.rings["Damage +3"] = (100, 3, 0)
        self.rings["Defense +1"] = (20, 0, 1)
        self.rings["Defense +2"] = (40, 0, 2)
        self.rings["Defense +3"] = (80, 0, 3)

    def solve(self):
        playerHP = 100
        enemyHP = self.ins[0]
        enemyDamage = self.ins[1]
        enemyArmor = self.ins[2]
        seen = set()
        totalCosts = set() # weapon, armor, ring 1, ring 2, cost
        for w in self.weapons:
            for a in self.armor:
                # choose 0-2 rings
                for r1 in self.rings:
                    for r2 in self.rings:
                        if r1 == r2 and r1 != "Nothing":
                            continue
                        if (w, a, r2, r1) in seen or (w, a, r1, r2) in seen:
                            continue
                        seen.add((w, a, r1, r2))
                        playerDamage = self.weapons[w][1] + self.rings[r1][1] + self.rings[r2][1]
                        playerArmor = self.armor[a][2] + self.rings[r1][2] + self.rings[r2][2]

                        # BATTLE
                        turn = 1
                        curPlayerHP = playerHP
                        curEnemyHP = enemyHP
                        enemyDamageReceive = playerDamage - enemyArmor # per turn
                        if enemyDamageReceive <= 0:
                            enemyDamageReceive = 1
                        playerDamageReceive = enemyDamage - playerArmor
                        if playerDamageReceive <= 0:
                            playerDamageReceive = 1
                        # print(f"BATTLE!! {(w, a, r1, r2)}")
                        while curPlayerHP > 0 and curEnemyHP > 0:
                            # print(f"Turn {turn}: Player HP: {curPlayerHP}, Enemy HP: {curEnemyHP}")
                            curEnemyHP -= enemyDamageReceive
                            if curEnemyHP <= 0:
                                break
                            curPlayerHP -= playerDamageReceive
                            turn += 1

                        cost = self.weapons[w][0] + self.armor[a][0] + self.rings[r1][0] + self.rings[r2][0]
                        if curEnemyHP <= 0:
                            # player wins
                            totalCosts.add((w, a, r1, r2, cost))
                        else:
                            totalCosts.add((w, a, r1, r2, -cost))
                            pass
        minGold = 999999999
        minSet = ()
        maxGold = -1
        maxSet = ()
        for c in totalCosts:
            if c[4] >= 0 and c[4] < minGold:
                minSet = c
                minGold = c[4]
            if c[4] <= 0 and -c[4] >= maxGold:
                maxSet = c
                maxGold = -c[4]
        print(f"Set that defeated the enemy: {minSet}")
        print(f"Most costly set that still made you lose: {maxSet}")

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
