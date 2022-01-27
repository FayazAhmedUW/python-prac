Class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

Class Graph:

    def __init__(self, nodes):
        self.nodes = []


    def colorGraph(self, graph, colors)
        for node in graph:
            if(node in none.neighbors):
                raise Exception("Impossible to have legal coloring with loop")


            illegals = [neighbour.color in node.neighbours if neighbour.color]

            for color in colors:
                if color not in illegals:
                    node.color = color
                    break


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')
h = GraphNode('h')
i = GraphNode('i')
j = GraphNode('j')
k = GraphNode('k')
l = GraphNode('l')

a.neighbours.add(b)
a.neighbours.add(c)
a.neighbours.add(d)
b.neighbours.add(a)
b.neighbours.add(f)
b.neighbours.add(g)
c.neighbours.add(a)
c.neighbours.add(d)
c.neighbours.add(h)
d.neighbours.add(a)
d.neighbours.add(c)
d.neighbours.add(e)
e.neighbours.add(d)
e.neighbours.add(f)
e.neighbours.add(j)
f.neighbours.add(b)
f.neighbours.add(e)
f.neighbours.add(g)
g.neighbours.add(b)
g.neighbours.add(f)
g.neighbours.add(k)
h.neighbours.add(c)
h.neighbours.add(i)
h.neighbours.add(l)
i.neighbours.add(h)
i.neighbours.add(j)
i.neighbours.add(l)
j.neighbours.add(e)
j.neighbours.add(i)
j.neighbours.add(k)
k.neighbours.add(g)
k.neighbours.add(j)
k.neighbours.add(l)
l.neighbours.add(h)
l.neighbours.add(i)
l.neighbours.add(k)

colors = [red, green, blue, yellow]

testGraph = new Graph([a, b, c, d, e, f, g, h, i, j, k, l])

testGraph.colorGraph()
