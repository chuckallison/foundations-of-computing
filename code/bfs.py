# Python breadth-first traversal of Figure 8–19
import collections

class Node:
    def __init__(self, name, children=[]):
        self.visited = False
        self.name = name
        self.children = children

def bfs(node):
    # Initialize queue with start node
    q = collections.deque()
    q.append(node)

    while q:
        node = q.popleft()
        if not node.visited:
            # Visit node
            node.visited = True
            print('visited', node.name)

            # Add this node's child nodes (if not visited yet)
            for c in node.children:
                q.append(c)

id0 = Node("ID0")
id11 = Node("ID-1–1")
id12 = Node("ID-1–2")
id211 = Node("ID-2–1-1")
id212 = Node("ID-2–1-2")
id213 = Node("ID-2–1-3")
id214 = Node("ID-2–1-4")
id221 = Node("ID-2–2-1")
id222 = Node("ID-2–2-2")
id223 = Node("ID-2–2-3")
id3211 = Node("ID-3–2-1–1")

id0.children = [id11, id12]
id11.children = [id211, id212, id213, id214]
id12.children = [id221, id222, id223]
id211.children = [id3211]

bfs(id0)
