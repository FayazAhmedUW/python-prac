Class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

    def colorGraph(self, graph, colors)
        for node in graph:
            if(node in none.neighbors):
                raise Exception("Impossible to have legal coloring with loop")


            illegals = [neighbour.color in node.neighbours if neighbour.color]

            for color in colors:
                if color not in illegals:
                    node.color = color
                    break


testGraph =
