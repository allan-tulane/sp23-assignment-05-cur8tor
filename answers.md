# CMPS 2200 Assignment 5
## Answers

**Name:**_____Tanner Martz_______


Place all written answers from `assignment-05.md` here for easier grading.


- **1a.**

Greedy sudo code:
```
function(N, coin_count = 0):
  if 0 == N:
    return coin_count
  
  largest_coin = 2 ^ floor(log2(N))
  remaining_dollars = N - largest_coin
  
  return function(remaining_dollars, coin_count++)
```
This algo produced the optimal number of coins needed for N dollars. 

- **1b.**

W(n) = W(n - n^lg(n)) + 1
S(n) = S(n - n^lg(n)) + 1

- **2a.**

Given the set of denominations: {{1, 2, 4, 8}, {1, 10, 100}}
If N = 118, the greedy algorithum will scan denominations from largest to smallest:
0 + 100 = 100 -> 100 + 10 -> = 110 -> 110 + 1 = 110 -> 111 + 4 = 115 
-> 115 + 2 = 117 -> 117 + 1 = 118 
100 + 10 + 1 + 4 + 2 + 1 = 118
This prodcued a coin count of 6, however the optimal coin count is 3. 
100 + 10 + 8 = 118

Greedy algorithum does not produce the optimal number of coins because the 
set of denominations is not constant across banks. Therefore multiple 
sub problems must be solved for each bank inorder to prodcue the optimal number
of coins. 

- **2b.**

Let k = the number of denominations, n = the dollar ammount
W(n) = O(n * k)
S(n) = O(n)

- **3a.**
```
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
```
- **3b.**

```
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
```

- **3c.**

```
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
```