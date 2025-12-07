class Container:
    def __init__(self):
        self.amount = 0.0
        self.neighbors = set()

    def getAmount(self):
        return self.amount

    def connectTo(self, other):
        if other is self or other in self.neighbors:
            return
        self.neighbors.add(other)
        other.neighbors.add(self)
        self._redistribute()

    def disconnectFrom(self, other):
        if other not in self.neighbors:
            return
        self.neighbors.remove(other)
        other.neighbors.remove(self)
        self._redistribute()
        other._redistribute()

    def addWater(self, value):
        self.amount += value
        self._redistribute()

    def _redistribute(self):
        group = []
        seen = set()
        stack = [self]
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            group.append(n)
            stack.extend(n.neighbors)
        total = sum(x.amount for x in group)
        each = total / len(group)
        for x in group:
            x.amount = each


def printState(name, containers):
    print(name)
    for key, c in containers.items():
        print(f"{key}: {c.getAmount():.2f}")
    print("-" * 35)


if __name__ == "__main__":
    A = Container()
    B = Container()
    C = Container()
    D = Container()
    E = Container()
    F = Container()
    G = Container()

    allC = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G}

    A.addWater(10)
    B.addWater(30)
    C.addWater(5)
    D.addWater(100)
    E.addWater(40)
    F.addWater(200)
    G.addWater(1)

    printState("Initial amounts", allC)

    A.connectTo(B)
    B.connectTo(C)
    printState("A-B-C linked", allC)

    D.connectTo(E)
    E.connectTo(F)
    printState("D-E-F linked", allC)

    A.connectTo(D)
    printState("Full merge of ABC with DEF", allC)

    G.addWater(9)
    printState("Only G affected (isolated)", allC)

    G.connectTo(C)
    printState("G merged with large component", allC)

    F.disconnectFrom(E)
    printState("Disconnect F-E: two components rebalance independently", allC)

    A.disconnectFrom(B)
    printState("Disconnect A-B: multiple components split", allC)

    C.addWater(50)
    printState("Add 50 to C's new component", allC)

    D.connectTo(G)
    printState("Connect D-G to merge two components again", allC)
