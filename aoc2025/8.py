QUIZ_NUMBER = "8"

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
        for i in range(0, len(arr)-1):
            line = list(map(int, arr[i].split(',')))
            self.ins.append(line[::])
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        len_arr = []
        for i in range(len(self.ins)):
            len_arr.append([0 for j in range(len(self.ins))])

        # calculate all distances between nodes
        for i in range(len(self.ins)):
            for j in range(i+1, len(self.ins)):
                if i == j:
                    continue
                len_arr[i][j] = (self.ins[i][0] - self.ins[j][0])**2 + \
                                (self.ins[i][1] - self.ins[j][1])**2 + \
                                (self.ins[i][2] - self.ins[j][2])**2

        # put distances with which nodes are connect into an array and sort
        node_arr = []
        for i in range(len(self.ins)):
            for j in range(i+1, len(self.ins)):
                node_arr.append([len_arr[i][j], i, j])
        sorted_node_arr = sorted(node_arr, key=lambda x: x[0])
        


        # start connecting them, put circuit into a set from an array of all sets
        cs = []
        cnt = 0
        for cur_node in sorted_node_arr:
            n1, n2 = tuple(self.ins[cur_node[1]]), tuple(self.ins[cur_node[2]])
            # print(cnt, cur_node, n1, n2, cs)
            if cnt == 1000:
                break
            if not cs:
                s = set()
                s.add(n1)
                s.add(n2)
                cs.append(s)
                cnt += 1
            else:
                a = n1
                b = n2

                found_a_c = -1
                found_b_c = -1
                for ci in range(len(cs)):
                    c = cs[ci]
                    if a in c:
                        found_a_c = ci
                    if b in c:
                        found_b_c = ci
                if found_a_c != -1 and found_b_c != -1 and found_a_c != found_b_c:
                    # both found, different sets/circuits
                    old_ac = cs[found_a_c]
                    old_bc = cs[found_b_c]
                    new_cs = []
                    for old_nci in range(len(cs)):
                        if old_nci == found_a_c or old_nci == found_b_c:
                            continue
                        else:
                            new_cs.append(cs[old_nci])
                    old_ac = old_ac.union(old_bc)
                    new_cs.append(old_ac)
                    # print("HELLO", old_ac, old_bc)
                    cs = new_cs[::]
                    cnt += 1
                elif found_a_c != -1 and found_a_c != found_b_c:
                    # only a found
                    cs[found_a_c].add(b)
                    cnt += 1
                elif found_b_c != -1 and found_a_c != found_b_c:
                    # only b found
                    cs[found_b_c].add(a)
                    cnt += 1
                elif found_a_c == found_b_c and found_a_c == -1:
                    # both not found
                    ns = set()
                    ns.add(b)
                    ns.add(a)
                    cs.append(ns)
                    cnt += 1
                else:
                    cnt += 1
            # total_size = 0
            # for c in cs:
            #     total_size += len(c)
            # if total_size == len(self.ins):
            #     break
        result = 1
        sizes = []
        for c in cs:
            sizes.append(len(c))
            # print(c, len(c))
        sizes.sort()
        # print(sizes)
        for s in range(len(sizes)-1,len(sizes)-1-3,-1):
            result *= sizes[s]
        # print(cs)
        print(f"{result}")

    def solve2(self):
        print("--- Part Two ---")
        len_arr = []
        for i in range(len(self.ins)):
            len_arr.append([0 for j in range(len(self.ins))])

        # calculate all distances between nodes
        for i in range(len(self.ins)):
            for j in range(i+1, len(self.ins)):
                if i == j:
                    continue
                len_arr[i][j] = (self.ins[i][0] - self.ins[j][0])**2 + \
                                (self.ins[i][1] - self.ins[j][1])**2 + \
                                (self.ins[i][2] - self.ins[j][2])**2

        # put distances with which nodes are connect into an array and sort
        node_arr = []
        for i in range(len(self.ins)):
            for j in range(i+1, len(self.ins)):
                node_arr.append([len_arr[i][j], i, j])
        sorted_node_arr = sorted(node_arr, key=lambda x: x[0])
        


        # start connecting them, put circuit into a set from an array of all sets
        cs = []
        cnt = 0
        for cur_node in sorted_node_arr:
            n1, n2 = tuple(self.ins[cur_node[1]]), tuple(self.ins[cur_node[2]])
            # print(cnt, cur_node, n1, n2, cs)
            # if cnt == 1000:
            #     break
            # total_size = 0
            # for c in cs:
            #     total_size += len(c)
            if not cs:
                s = set()
                s.add(n1)
                s.add(n2)
                cs.append(s)
                cnt += 1
            else:
                a = n1
                b = n2

                found_a_c = -1
                found_b_c = -1
                for ci in range(len(cs)):
                    c = cs[ci]
                    if a in c:
                        found_a_c = ci
                    if b in c:
                        found_b_c = ci
                if found_a_c != -1 and found_b_c != -1 and found_a_c != found_b_c:
                    print(f"A {cnt}")
                    # both found, different sets/circuits
                    old_ac = cs[found_a_c]
                    old_bc = cs[found_b_c]
                    new_cs = []
                    for old_nci in range(len(cs)):
                        if old_nci == found_a_c or old_nci == found_b_c:
                            continue
                        else:
                            new_cs.append(cs[old_nci])
                    old_ac = old_ac.union(old_bc)
                    new_cs.append(old_ac)
                    # print("HELLO", old_ac, old_bc)
                    cs = new_cs[::]
                    if len(cs) == 1 and len(cs[0]) == len(self.ins):
                        print(a[0]*b[0])
                        return
                    cnt += 1
                elif found_a_c != -1 and found_a_c != found_b_c:
                    print(f"B {cnt}")
                    # only a found
                    cs[found_a_c].add(b)
                    print(a[0]*b[0])
                    cnt += 1
                elif found_b_c != -1 and found_a_c != found_b_c:
                    print(f"C {cnt}")
                    # only b found
                    cs[found_b_c].add(a)
                    cnt += 1
                elif found_a_c == found_b_c and found_a_c == -1:
                    print(f"D {cnt}")
                    # both not found
                    ns = set()
                    ns.add(b)
                    ns.add(a)
                    cs.append(ns)
                    cnt += 1
                else:
                    # print(f"E {cnt}")
                    cnt += 1
        # print(len(cs), len(cs[0]), len(self.ins))
        # result = 1
        # sizes = []
        # for c in cs:
        #     sizes.append(len(c))
        #     print(c, len(c))
        # sizes.sort()
        # print(sizes)
        # for s in range(len(sizes)-1,len(sizes)-1-3,-1):
        #     result *= sizes[s]
        # print(cs)
        

def main():
    # Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
