class WeatherMachine:
    def test(fileName = "1.ex.in"):
        weatherMachine = WeatherMachine(fileName)
        weatherMachine.getCalibrationValues()

    def solve1():
        WeatherMachine.test("1.in")

    def __init__(self, fileName):
        self.ins = []
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split()))
        for i in range(0, len(arr)):
            self.ins.append(arr[i])
        fp.close()

    def getCalibrationValues(self):
        calibrationValues = []
        for i in range(len(self.ins)):
            calibrationValues.append(self.getCalibrationValue(i))
        self.print(calibrationValues)

    def getCalibrationValue(self, i):
        line = self.ins[i]
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(int(line[i]))
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                digits.append(int(line[i]))
                break
        value = 0
        for i in range(len(digits)):
            value *= 10
            value += digits[i]
        return value

    def print(self, values):
        for (i, value) in enumerate(values):
            print("Calibration value for line", i, ":", value)
        print("Calibration values:", sum(values))

# WeatherMachine.test()
WeatherMachine.solve1()