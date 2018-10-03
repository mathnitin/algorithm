#!/bin/python

from collections import defaultdict

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths


# Define graph by edges
edges = [['1', '2'], ['2', '4'], ['1', '11'], ['4', '11']]

# Build graph dictionary
G = defaultdict(list)
for (s,t) in edges:
    G[s].append(t)
    G[t].append(s)

# Run DFS, compute metrics
all_paths = DFS(G, '1')
max_len   = max(len(p) for p in all_paths)
max_paths = [p for p in all_paths if len(p) == max_len]

# Output
print("All Paths:")
print(all_paths)
print("Longest Paths:")
for p in max_paths: print("  ", p)
print("Longest Path Length:")
print(max_len)