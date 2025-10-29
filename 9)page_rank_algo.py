
# EXPERIMENT NO: 09
# AIM: Implementation of the PageRank Algorithm using Python

import numpy as np
import networkx as nx

# -----------------------------
# Step 1: Represent Web Graph
# -----------------------------
# Example web structure (directed graph)
# A -> B, A -> C, B -> C, C -> A
pages = ['A', 'B', 'C']
links = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A']
}

# Create adjacency matrix
n = len(pages)
M = np.zeros((n, n))

for i, page in enumerate(pages):
    if len(links[page]) > 0:
        for linked_page in links[page]:
            j = pages.index(linked_page)
            M[j][i] = 1 / len(links[page])

print("Adjacency Matrix (M):")
print(M)

# -----------------------------
# Step 2: Initialize Parameters
# -----------------------------
d = 0.85  # Damping factor
ranks = np.ones(n) / n  # Initial equal ranks
tolerance = 1e-6  # Convergence tolerance

# -----------------------------
# Step 3: Iteratively Calculate PageRank
# -----------------------------
for iteration in range(100):
    new_ranks = (1 - d) / n + d * M.dot(ranks)
    if np.linalg.norm(new_ranks - ranks, 1) < tolerance:
        print(f"\nConverged after {iteration + 1} iterations.")
        break
    ranks = new_ranks

# -----------------------------
# Step 4: Display Results
# -----------------------------
print("\nFinal PageRank Values:")
for i, page in enumerate(pages):
    print(f"Page {page}: {ranks[i]:.4f}")

# -----------------------------
# Step 5: Compare with NetworkX PageRank
# -----------------------------
G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')])
nx_ranks = nx.pagerank(G, alpha=d)
print("\nNetworkX PageRank Results:")
for page, rank in nx_ranks.items():
    print(f"Page {page}: {rank:.4f}")
