QUIZ_NUMBER = "22"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        print("===", fileName, "===")
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(int, fp.read().split(',')))
        fp.close()
        self.enemyHP = arr[0]
        self.enemyDamage = arr[1]
        self.playerHP = 50
        self.playerMP = 500
        self.spells = dict()
        # cost, damage to enemy
        self.spells["Magic Missile"] = (53, 4)
        # cost, damage to enemy, heal to player
        self.spells["Drain"] = (73, 2, 2)
        # cost, turns last, armor increase while turns last
        self.spells["Shield"] = (113, 6, 7)
        # cost, turns last, damage to enemy per turn while turns last
        self.spells["Poison"] = (173, 6, 3)
        # cost, turns last, new mana at start of turn per turn while turns last
        self.spells["Recharge"] = (229, 5, 101)

    def solve1(self):
        print("--- Part One ---")
        self.outcomes = set()
        self.minMP = 9999999
        def backtrack(turn, effects, pHP, pMP, eHP, totalMPCost):
            if eHP <= 0:
                if self.minMP > totalMPCost:
                    print(f"Won at turn {turn} with MP cost: {totalMPCost}")
                self.minMP = min(self.minMP, totalMPCost)
            if pHP <= 0:
                return
            if pMP < 53 and effects[2] == 0:
                return

            if turn > 1:
                # effect
                pArmor = 0
                if effects[0] > 0:
                    effects[0] -= 1
                    pArmor = self.spells["Shield"][2]
                if effects[1] > 0:
                    effects[1] -= 1
                    eHP -= self.spells["Poison"][2]
                if effects[2] > 0:
                    effects[2] -= 1
                    pMP += self.spells["Recharge"][2]

                # enemy's turn
                playerReceiveDamage = self.enemyDamage - pArmor
                playerReceiveDamage = 1 if playerReceiveDamage <= 0 else playerReceiveDamage
                pHP -= playerReceiveDamage
                turn += 1
                if pHP <= 0:
                    return

            # effect
            pArmor = 0
            if effects[0] > 0:
                effects[0] -= 1
                pArmor = self.spells["Shield"][2]
            if effects[1] > 0:
                effects[1] -= 1
                pHP -= self.spells["Poison"][2]
            if effects[2] > 0:
                effects[2] -= 1
                pMP += self.spells["Recharge"][2]

            # player's turn
            turn += 1
            s = "Magic Missile"
            backtrack(turn, effects[:], pHP, pMP-self.spells[s][0], eHP-self.spells[s][1], totalMPCost+self.spells[s][0])
            s = "Drain"
            backtrack(turn, effects[:], pHP+self.spells[s][2], pMP-self.spells[s][0], eHP-self.spells[s][1], totalMPCost+self.spells[s][0])
            s = "Shield"
            newEffects = effects[:]
            newEffects[0] = self.spells[s][1]
            backtrack(turn, newEffects[:], pHP, pMP-self.spells[s][0], eHP, totalMPCost+self.spells[s][0])
            s = "Poison"
            newEffects = effects[:]
            newEffects[1] = self.spells[s][1]
            backtrack(turn, newEffects[:], pHP, pMP-self.spells[s][0], eHP, totalMPCost+self.spells[s][0])
            s = "Recharge"
            newEffects = effects[:]
            newEffects[2] = self.spells[s][1]
            backtrack(turn, newEffects[:], pHP, pMP-self.spells[s][0], eHP, totalMPCost+self.spells[s][0])



        effects = [0, 0, 0] # shield, poison, recharge
        backtrack(1, effects[:], self.playerHP, self.playerMP, self.enemyHP, 0)
        print(f"Least amount of mana spent to win the fight: {0}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    # testSol = Solution(QUIZ_NUMBER + ".ex.in")
    # testSol.playerHP = 10
    # testSol.playerMP = 250
    # testSol.solve1()
    Solution.run()

if __name__ == "__main__":
    main()
