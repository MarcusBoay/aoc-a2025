class ScratchCards:
    def test(fileName = "4.ex.in"):
        scratchCards = ScratchCards(fileName)
        scratchCards.solve1()
        scratchCards.solve2()

    def run():
        ScratchCards.test("4.in")

    def __init__(self, fileName):
        self.ins = []
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split('|')
            self.ins.append(line[::])
        fp.close()

    def solve1(self):
        print("--- Part One ---")
        totalPoints = 0
        for (i, card) in enumerate(self.ins):
            print("==", "Card", i, "==")
            # print(card)
            winningNumbers = list(map(int, card[0].split()))
            foundWinningNumbers = []
            for number in list(map(int, card[1].split())):
                if number in winningNumbers:
                    foundWinningNumbers.append(number)
            print("found winning numbers:", foundWinningNumbers)
            if foundWinningNumbers:
                totalPoints += 1 << (len(foundWinningNumbers) - 1)
        print("=== Total Points ===")
        print(totalPoints)

    def solve2(self):
        print("--- Part Two ---")
        totalCards = [1] * len(self.ins)
        for (i, card) in enumerate(self.ins):
            print("==", "Card", i, "==")
            print("Total Cards:", totalCards)
            winningNumbers = list(map(int, card[0].split()))
            numberOfWinningNumbers = 0
            for number in list(map(int, card[1].split())):
                if number in winningNumbers:
                    numberOfWinningNumbers += 1
            print("Number of winning numbers:", numberOfWinningNumbers)
            for winNumber in range(i+1, numberOfWinningNumbers+i+1):
                totalCards[winNumber] += totalCards[i]
        print("=== Total Cards ===")
        print(totalCards)
        print("Sum:", sum(totalCards))


ScratchCards.test()
ScratchCards.run()