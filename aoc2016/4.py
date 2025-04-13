QUIZ_NUMBER = "4"
import re

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
            self.ins.append(arr[i][:])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        sumOfSectorIDs = 0
        for room in self.ins:
            # get checksum
            checksum = set()
            for i in range(len(room)-6, len(room)-1):
                checksum.add(room[i])

            # get sector id
            room = room[0:len(room)-7].split('-')
            sectorID = int(room.pop())

            # get count of all letters
            letters = [0] * 26
            for words in room:
                for c in words:
                    letters[ord(c) - ord('a')] += 1

            common = [] # most common letters in descending order
            seenI = set()
            seenN = set()
            while len(common) < 5:
                # get nth most common letter
                n = 0
                for i in range(len(letters)):
                    if i not in seenI and letters[i] not in seenN and letters[i] > n:
                        n = letters[i]
                seenN.add(n)

                # get all nth most common letter
                for i in range(len(letters)):
                    if i not in seenI and letters[i] == n:
                        common.append(i)

            isRealRoom = True
            for i in range(5):
                if chr(common[i]+ord('a')) not in checksum:
                    isRealRoom = False
                    break

            if isRealRoom:
                sumOfSectorIDs += sectorID

        print("Sum of sector IDs:", sumOfSectorIDs)



    def solve2(self):
        print("--- Part Two ---")
        for room in self.ins:
            # get checksum
            checksum = set()
            for i in range(len(room)-6, len(room)-1):
                checksum.add(room[i])

            # get sector id
            room = room[0:len(room)-7].split('-')
            sectorID = int(room.pop())
            shift = sectorID % 26

            decryptedWords = []
            for word in room:
                d = ""
                for e in word:
                    d += chr(((ord(e) - ord('a') + shift) % 26) + ord('a'))
                decryptedWords.append(d)
            if (decryptedWords[0] == "northpole"):
                print(decryptedWords, sectorID)




def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
