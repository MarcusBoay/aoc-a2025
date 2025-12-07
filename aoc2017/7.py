QUIZ_NUMBER = "7"

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

        # get hashmap of nodes (name: weight)
        self.nodes = dict()
        self.nodeRelationship = dict()
        for row in self.ins:
            self.nodes[row[0]] = int(row[1])
            self.nodeRelationship[row[0]] = []
            for child in row[2::]:
                self.nodeRelationship[row[0]].append(child)
        # print(self.nodes)
        # print(self.nodeRelationship)

    def solve1(self):
        print("--- Part One ---")

        # get all parents and childrens
        children = set()
        parents = set()
        for row in self.ins:
            if len(row) > 2:
                parents.add(row[0])
                i = 2
                while i < len(row):
                    children.add(row[i])
                    i += 1

        # remove all parents who are also children
        for child in children:
            if child in parents:
                parents.remove(child)

        print("Bottom program:", parents)
        for p in parents:
            self.root = p

    def solve2(self):
        print("--- Part Two ---")
        def createTree(root):
            for childName in self.nodeRelationship[root.name]:
                child = Node(self.nodes[childName], childName)
                root.children.append(child)
                createTree(child)

        def getSumWeight(root):
            if not root:
                return 0
            if not root.children:
                return root.weight

            s = 0
            for c in root.children:
                s += getSumWeight(c)
            return s + root.weight

        # create tree
        p = self.root
        self.root = Node(self.nodes[p], p)
        createTree(self.root)

        q = [self.root]
        prevWeight = 0
        prevNode = self.root
        while q:
            qn = len(q)
            while qn:
                qn -= 1
                cur = q.pop(0)

                ws = []
                for i in range(len(cur.children)):
                    c = cur.children[i]
                    w = getSumWeight(c)
                    ws.append(w)
                print(ws)
                heavier = 0
                lighter = 999999999999
                for cw in ws:
                    if heavier < cw:
                        heavier = cw
                    if lighter > cw:
                        lighter = cw
                if lighter < heavier:
                    ci = 99999
                    for i in range(len(ws)):
                        if ws[i] == heavier:
                            ci = i
                            break
                    q.append(cur.children[ci])
                    prevWeight = heavier
                    prevNode = cur.children[ci]
                else:
                    # current level is balanced
                    print(prevWeight, prevNode.name, prevNode.weight)

class Node:
    def __init__(self, w, name):
        self.weight = w
        self.name = name
        self.children = []

def main():
    Solution.test()
    Solution.run()

if __name__ == "__main__":
    main()
