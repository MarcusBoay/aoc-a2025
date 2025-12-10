QUIZ_NUMBER = "10"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.ins = []
        self.lights = []
        self.button_wiring = []
        self.joltage = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)-1):
            line = arr[i].split(' ')
            self.lights.append(list(line[0][1:-1]))
            self.joltage.append(list(map(int, line[-1][1:-1].split(','))))
            buttons = line[1:-1]
            formatted_buttons = []
            for b in buttons:
                formatted_buttons.append(list(map(int, b[1:-1].split(','))))
            self.button_wiring.append(formatted_buttons)
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        total_fewest_presses = 0
        for pi in range(len(self.lights)):
            seen_l = set()
            # seen_r = set()
            target_lights = "".join(self.lights[pi])
            buttons = self.button_wiring[pi]

            q = [['.'] * len(target_lights)]
            fewest_button_presses = 0
            seen_l.add("".join(q[0]))
            found = False
            while not found:
                qn = len(q)
                fewest_button_presses += 1
                while qn and not found:
                    qn -= 1
                    cur = q.pop(0)
                    for presses in buttons:
                        next = cur[::]
                        # print(next)
                        # print(presses)
                        for press in presses:
                            press = int(press)
                            if next[press] == '.':
                                next[press] = '#'
                            else:
                                next[press] = '.'
                        if "".join(next) not in seen_l:
                            q.append(next[::])
                            seen_l.add("".join(next))
                        if target_lights == "".join(next):
                            print(f"Fewest button presses for problem {pi+1}: {fewest_button_presses}")
                            total_fewest_presses += fewest_button_presses
                            found = True
                            break
        print(f"Total fewest button presses: {total_fewest_presses}")

    def solve2(self):
        print("--- Part Two ---")

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
