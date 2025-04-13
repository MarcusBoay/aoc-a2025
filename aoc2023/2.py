class CubeGame:
    def test(fileName = "2.ex.in"):
        cubeGame = CubeGame(fileName)
        cubeGame.solve1()
        cubeGame.solve2()

    def run():
        CubeGame.test("2.in")

    def __init__(self, fileName):
        self.ins = []
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            self.ins.append(arr[i])
        if (self.ins[-1] == ""):
            self.ins.pop()
        fp.close()

    def solve1(self):
        ids = []
        for i in range(len(self.ins)):
            loaded = [12, 13, 14] # R G B
            line = self.ins[i][::]
            line = line.split(":")
            id = line.pop(0)
            line = line[0].split(";")
            ids.append(i+1)
            # print("id:", i)
            for (i, play) in enumerate(line):
                # print("play", i)
                play = play.strip().split(", ")
                isGameFoul = False
                for pair in play:
                    pair = pair.split()
                    # print(pair)
                    if (pair[1] == 'red' and loaded[0] - int(pair[0]) < 0) or (pair[1] == 'green' and loaded[1] - int(pair[0]) < 0) or (pair[1] == 'blue' and loaded[2] - int(pair[0]) < 0):
                        # print("popping", i)
                        ids.pop()
                        isGameFoul = True
                        break
                if isGameFoul:
                    break
        print(ids)
        print("sum:", sum(ids))

    def solve2(self):
        powers = []
        for i in range(len(self.ins)):
            power = [0, 0, 0] # R G B
            line = self.ins[i][::]
            line = line.split(":")
            id = line.pop(0)
            line = line[0].split(";")
            # print("id:", i)
            for (i, play) in enumerate(line):
                # print("play", i)
                play = play.strip().split(", ")
                for pair in play:
                    pair = pair.split()
                    # print(pair)
                    if pair[1] == 'red':
                        power[0] = max(int(pair[0]), power[0])
                    elif pair[1] == 'green':
                        power[1] = max(int(pair[0]), power[1])
                    elif pair[1] == 'blue':
                        power[2] = max(int(pair[0]), power[2])
            powers.append(power[0]*power[1]*power[2])
        print(powers)
        print("sum:", sum(powers))

    # def print(self, values):
    #     for (i, value) in enumerate(values):
    #         print("Calibration value for line", i, ":", value)
    #     print("Calibration values:", sum(values))

CubeGame.test()
CubeGame.run()