QUIZ_NUMBER = "4"

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
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = arr[i].split()
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        validPassphrases = 0
        for passphrase in self.ins:
            wordsSeen = set()
            isValid = True
            for word in passphrase:
                if word in wordsSeen:
                    isValid = False
                    break
                wordsSeen.add(word)
            if isValid:
                validPassphrases += 1
        print("Number of valid passphrases:", validPassphrases)

    def solve2(self):
        print("--- Part Two ---")
        validPassphrases = 0
        for passphrase in self.ins:
            isValid = True
            for i in range(len(passphrase)):
                print("Searching:", passphrase[i])
                p1 = [0]*26
                for c in passphrase[i]:
                    p1[ord(c) - ord('a')] += 1

                for j in range(i+1, len(passphrase)):
                    p2 = p1[::]
                    for c in passphrase[j]:
                        p2[ord(c) - ord('a')] -= 1
                    isCurValid = False
                    for k in p2:
                        if k != 0: # valid
                            isCurValid = True
                            break
                    if not isCurValid:
                        isValid = False
                if not isValid:
                    break
            if isValid:
                validPassphrases += 1
            # print("Passphrase:", passphrase)
            # print("Is valid:", isValid)
        print("Number of valid passphrases:", validPassphrases)

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
