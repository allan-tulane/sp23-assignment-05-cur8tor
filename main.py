from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    print(f"Init Node: {start_node}\n")
    while len(frontier) != 0:

        start_node = frontier.pop()
        print(f"Root Node: {start_node}")

        neighbors = graph[start_node]
        print(f"Neighbor nodes: {neighbors}\n")

        for leaf in neighbors: 
          if leaf not in result:
            frontier.add(leaf)
          result.add(leaf)    
        print(f"Visted nodes: {result}")
        print(f"Nodes in queue: {frontier}\n")
       
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']

def connected(graph):
    g_nodes = list(graph.keys())
    reach = reachable(graph, g_nodes[0])
    if reach == set(g_nodes):
      print("Graph is connected")
      return True
    else:
      print(f"Nodes {reach} disconnected from graph")
      return False

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False

def n_components(graph):
    g = list(graph.keys())
    print(f"Nodes in graph: {g}\n")

    r = reachable(graph, g[0])
    sub_g = [r]
    sub_g_visited = r
    print(f"Init sub-graph nodes visited: {sub_g_visited}")

    while set(g) != sub_g_visited:
      sub_g_diff = set(g) - sub_g_visited
      print(f"Unrechable nodes from visited sub-graphs: {sub_g_diff}\n")
      
      r = reachable(graph, list(sub_g_diff)[0])
      sub_g.append(r)
      sub_g_visited = set().union(*sub_g)
      print(f"Visited sub-graph nodes: {sub_g_visited}")

    return len(sub_g)

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2

test_n_components()
test_reachable()
test_connected()