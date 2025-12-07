# 0 = N, 1 = W, 2 = S, 3 = E
DIRECTIONS = ['N', 'W', 'S', 'E']

class Ship:
    def test(fileName = "12.1.ex.in"):
        ship = Ship(fileName)
        ship.moveAll()
        ship.print()

    def __init__(self, fileName):
        self.ins = [[], []]
        self.pos = [0, 0] # y, x
        self.facing = 3 # direction the ship is facing, starts at EAST
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split()))
        for i in range(0, len(arr)):
            self.ins[0].append(arr[i][0])
            self.ins[1].append(int(arr[i][1::]))
        fp.close()

    # Moves based on what is in self.ins[actionIndex]
    def move(self, actionIndex):
        action = self.ins[0][actionIndex]
        value = self.ins[1][actionIndex]
        print("Moving... action:", action, "value:", value)
        if action == 'N':
            self.pos[0] -= value
        elif action == 'S':
            self.pos[0] += value
        elif action == 'E':
            self.pos[1] += value
        elif action == 'W':
            self.pos[1] -= value
        elif action == 'L':
            value //= 90
            self.facing = (self.facing + value) % 4
        elif action == 'R':
            value //= 90
            self.facing = (self.facing - value) % 4
        elif action == 'F':
            if self.facing == 0:
                self.pos[0] -= value
            elif self.facing == 1:
                self.pos[1] -= value
            elif self.facing == 2:
                self.pos[0] += value
            elif self.facing == 3:
                self.pos[1] += value
        else:
            print("MALFORMED ACTION:", action, "ON LINE", actionIndex)
            exit(1)

    def moveAll(self):
        for i in range(0, len(self.ins[0])):
            self.print()
            self.move(i)

    def print(self):
        print("Position:", self.pos)
        print("Facing:", self.facing)
        print("Manhattan distance:", abs(self.pos[0]) + abs(self.pos[1]))

# Ship.test("12.x.in")
ship = Ship("12.1.in")
ship.moveAll()
ship.print()

