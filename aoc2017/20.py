import math


QUIZ_NUMBER = "20"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test():
        Solution.run(QUIZ_NUMBER + ".ex.in")

    def __init__(self, fileName):
        self.p = []
        self.v = []
        self.a = []
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)):
            line = list(map(int, arr[i].split(",")))
            self.p.append(line[0:3])
            self.v.append(line[3:6])
            self.a.append(line[6:9])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        minD = 999999999999
        minI = 0
        # s = ut + 0.5at^2
        t = 1000
        for i in range(len(self.p)):
            sx = self.v[i][0]*t + 0.5*self.a[i][0]*t*t
            sy = self.v[i][1]*t + 0.5*self.a[i][1]*t*t
            sz = self.v[i][2]*t + 0.5*self.a[i][2]*t*t
            sx += self.p[i][0]
            sy += self.p[i][1]
            sz += self.p[i][2]
            absS = abs(sx) + abs(sy) + abs(sz)
            if absS < minD:
                minD = absS
                minI = i
        print(f"Particle that will stay the closest to origin: {minI}")

    # failed because i didn't read the question on how distance and speed are calculated...
    def solve2(self):
        print("--- Part Two ---")
        # # s = u1*t + 0.5*a1*t^2 + s1
        # # s = u2*t + 0.5*a2*t^2 + s2
        # # assume they are equal
        # # u2*t + 0.5*a2*t^2 + s2 = u1*t + 0.5*a1*t^2 + s1
        # # ...
        # # t = (u2 - u1 +- sqrt((u1 - u2)^2 - 2(a1 - a2)(s1 - s2))) / (a1-a2)
        # # - the denominator must != 0.
        # # - the discriminant must >= 0.
        # #    - there can be two roots. imagine p1 is a constant velocity particle and p2 is a yoyo.
        # # 0 == D = (u1 - u2)^2 - 2(a1 - a2)(s1 - s2)
        # # ...
        # # D = u1^2 - 2*u2*u1 + u2^2 - 2(a1 - a2)(s1 - s2)
        # t = dict() # p1 : [[p2, t2], [p3, t3], ...]
        # maxT = 0
        # for i in range(len(self.p)):
        #     for j in range(i+1, len(self.p)):
        #         tij = []
        #         for xyzi in range(3):
        #             denom = self.a[i][xyzi] - self.a[j][xyzi]
        #             if denom == 0:
        #                 break
        #             discriminant = \
        #                 self.v[i][xyzi] * self.v[i][xyzi] - \
        #                 2*self.v[j][xyzi]*self.v[i][xyzi] + \
        #                 self.v[j][xyzi] * self.v[j][xyzi] - \
        #                 2*(self.a[i][xyzi]-self.a[j][xyzi])*(self.p[i][xyzi]-self.p[j][xyzi])
        #             if discriminant < 0:
        #                 break
        #             curTPos = (self.v[j][xyzi] - self.v[i][xyzi] + math.sqrt(discriminant)) // denom
        #             curTNeg = (self.v[j][xyzi] - self.v[i][xyzi] - math.sqrt(discriminant)) // denom
        #             tij.append([curTPos, curTNeg])
        #         if len(tij) == 3:
        #             for ti in tij[0]:
        #                 for tj in tij[1]:
        #                     for tk in tij[2]:
        #                         if ti < 0 or tj < 0 or tk < 0:
        #                             continue
        #                         if ti == tj == tk:
        #                             if i not in t:
        #                                 t[i] = []
        #                             t[i].append([j, ti])
        #                             maxT = max(maxT, ti)
        # # for p1 in t:
        # #     print(f"Particle {p1} has collisions: {t[p1]}")

        # # find collisions starting from t=0 up to maxT
        # collisions = set()
        # i = 0
        # while i <= maxT:
        #     curCollisions = set()
        #     for p in t:
        #         if p in collisions:
        #             continue
        #         for ct in t[p]:
        #             if ct[0] in collisions:
        #                 continue
        #              # allow collisions with same particle in the same tick
        #             if ct[1] == i:
        #                 print(f"Particles {i} and {ct[0]} collided at tick {i}")
        #                 print(f"{self.p[i]}, {self.v[i]}, {self.a[i]}")
        #                 print(f"{self.p[ct[0]]}, {self.v[ct[0]]}, {self.a[ct[0]]}")
        #                 curCollisions.add(i)
        #                 curCollisions.add(ct[0])
        #                 break
        #     collisions = collisions.union(curCollisions)
        #     i += 1
        # print(f"Number of collisions: {len(collisions)}")
        # print(f"Number of particles left: {len(self.p)-len(collisions)}")


def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
