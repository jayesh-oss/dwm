
# EXPERIMENT NO: 10
# AIM: Implementation of the HITS Algorithm using Python

import numpy as np
import networkx as nx

# -----------------------------
# Step 1: Represent Web Graph
# -----------------------------
# Example graph: A -> B, A -> C, B -> C, C -> A
pages = ['A', 'B', 'C']
n = len(pages)
adjacency_matrix = np.array([
    [0, 1, 1],  # A links to B, C
    [0, 0, 1],  # B links to C
    [1, 0, 0]   # C links to A
])

print("Adjacency Matrix:")
print(adjacency_matrix)

# -----------------------------
# Step 2: Initialize Scores
# -----------------------------
authority = np.ones(n)
hub = np.ones(n)
tolerance = 1e-6
max_iterations = 100

# -----------------------------
# Step 3: Iteratively Update Scores
# -----------------------------
for iteration in range(max_iterations):
    new_authority = adjacency_matrix.T.dot(hub)
    new_hub = adjacency_matrix.dot(new_authority)

    # Normalize
    new_authority = new_authority / np.linalg.norm(new_authority, 2)
    new_hub = new_hub / np.linalg.norm(new_hub, 2)

    # Check for convergence
    if np.allclose(authority, new_authority, atol=tolerance) and np.allclose(hub, new_hub, atol=tolerance):
        print(f"\nConverged after {iteration + 1} iterations.")
        break

    authority, hub = new_authority, new_hub

# -----------------------------
# Step 4: Display Final Scores
# -----------------------------
print("\nFinal Authority Scores:")
for i, page in enumerate(pages):
    print(f"Page {page}: {authority[i]:.4f}")

print("\nFinal Hub Scores:")
for i, page in enumerate(pages):
    print(f"Page {page}: {hub[i]:.4f}")

# -----------------------------
# Step 5: Verify with NetworkX
# -----------------------------
G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')])
hits_scores = nx.hits(G, max_iter=100, normalized=True)

print("\nNetworkX HITS Results:")
print("Authorities:", hits_scores[1])
print("Hubs:", hits_scores[0])
