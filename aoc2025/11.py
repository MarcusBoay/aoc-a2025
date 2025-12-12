import copy
import networkx as nx
import matplotlib.pyplot as plt
from itertools import product

QUIZ_NUMBER = "11"

class Solution:
    def run(fileName = QUIZ_NUMBER + ".in"):
        solution = Solution(fileName)
        solution.solve1()
        solution.solve2()

    def test1():
        solution = Solution(QUIZ_NUMBER + ".ex1.in")
        solution.solve1()

    def test2():
        solution = Solution(QUIZ_NUMBER + ".ex2.in")
        solution.solve2()

    def __init__(self, fileName):
        self.ins = dict()
        self.fileName = fileName
        fp = open(fileName, 'r')
        arr = list(map(str, fp.read().split('\n')))
        for i in range(0, len(arr)-1):
            line = arr[i].split(' ')
            line[0] = line[0][0:-1]
            self.ins[line[0]] = line[1::]
        fp.close()
        print("===", self.fileName, "===")

    def solve1(self):
        print("--- Part One ---")
        def backtrack(seen, cur):
            if cur == "out":
                self.paths += 1
                return

            for next in self.ins[cur]:
                seen.add(next)
                backtrack(seen, next)
                seen.remove(next)

        self.paths = 0
        seen = set()
        seen.add("you")
        backtrack(seen, "you")
        print(f"Number of paths: {self.paths}")

    def solve2(self):
        print("--- Part Two ---")
        def search(nodes, start, stop=None):
            found = False
            while not found:
                layer = nodes.pop(0)
                for n in layer:
                    if n == start:
                        found = True
                        break

            q = [start]
            while q:
                qn = len(q)
                while qn:
                    qn -= 1
                    cur = q.pop(0)
                    for cn in self.ins[cur]:
                        self.freq[cn] += self.freq[cur]
                if nodes:
                    q = nodes.pop(0)

            # flush out old result in next nodes from old calculations
            if not stop:
                return
            cq = [stop]
            c_seen = set()
            while cq:
                cqn = len(cq)
                while cqn:
                    cqn -= 1
                    cur_c = cq.pop(0)
                    c_seen.add(cur_c)
                    for cn in self.ins[cur_c]:
                        if cn != stop:
                            # print(f"{stop} clearing {cn}")
                            self.freq[cn] = 0
                        if cn not in c_seen:
                            c_seen.add(cn)
                            cq.append(cn)
            return

        def draw():
            seen = set()
            G = nx.DiGraph()
            for k, v in self.ins.items():
                G.add_node(k + " " + str(self.freq[k]))
                for vv in v:
                    G.add_node(vv + " " + str(self.freq[vv]), color='blue')
                    G.add_edge(k + " " + str(self.freq[k]), vv + " " + str(self.freq[vv]))
            options = {
                "width": 1,
                "node_size": 20,
                "font_size": 18,
                "font_color": "gray"
            }
            sorted_nodes = list(nx.topological_generations(G))
            subset_key = dict()
            for i in range(len(sorted_nodes)):
                subset_key[i] = sorted_nodes[i]
            pos = nx.multipartite_layout(G, subset_key=subset_key)
            nx.draw(G, pos, with_labels=True, **options)
            nx.draw_networkx_nodes(G, pos, nodelist=["fft" + " " + str(self.freq["fft"]), "dac" + " " + str(self.freq["dac"]), "out" + " " + str(self.freq["out"])], node_color="tab:red")
            plt.show()
            return

        def dfs(u, v):
            if u == v:
                return 1

            if (self.freq[u] != -1):
                return self.freq[u]

            count = 0
            for w in self.ins[u]:
                count += dfs(w, v)
            self.freq[u] = count
            return count

        def populate():
            # populate
            self.freq = dict()
            for k,v in self.ins.items():
                self.freq[k] = -1
                for next in v:
                    self.freq[next] = -1

        # DG = nx.DiGraph()
        # for k, v in self.ins.items():
        #     DG.add_node(k)
        #     for vv in v:
        #         DG.add_node(vv)
        #         DG.add_edge(k, vv)
        # sorted_nodes = list(nx.topological_generations(DG))

        self.ins["out"] = []
        # self.freq["svr"] = 1
        # self.freq["out"] = 0
        # search(copy.deepcopy(sorted_nodes[::]), "svr", "fft")
        # print(self.freq["fft"])
        # draw()
        # search(copy.deepcopy(sorted_nodes[::]), "fft", "dac")
        # print(self.freq["dac"])
        # draw()
        # search(copy.deepcopy(sorted_nodes[::]), "dac")
        # draw()
        # print(self.freq["out"])

        # lazy networkx implementation
        # fft_n = len(list(nx.all_simple_paths(DG, "svr", "fft")))
        # print(fft_n)
        # dac_n = len(list(nx.all_simple_paths(DG, "fft", "dac")))
        # print(dac_n)
        # out_n = len(list(nx.all_simple_paths(DG, "dac", "out")))
        # print(out_n)
        # print(fft_n*dac_n*out_n)
 
        populate()
        fft_n = dfs("svr", "fft")
        populate()
        dac_n = dfs("fft", "dac")
        populate()
        out_n = dfs("dac", "out")
        print(fft_n, dac_n, out_n, fft_n*dac_n*out_n)





def main():
    Solution.test1()
    Solution.test2()
    Solution.run()

if __name__ == "__main__":
    main()
