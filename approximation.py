#set covering problem

universe = {1, 2, 3, 4, 5}

sets = {
    "S1": {1, 2, 3},
    "S2": {2, 4},
    "S3": {3, 4, 5},
    "S4": {5}
}

uncovered = set(universe)
selected = []

while uncovered:

    # Find the set covering maximum uncovered elements
    best_set = max(
        sets,
        key=lambda s: len(sets[s] & uncovered)
    )

    # Add the best set
    selected.append(best_set)

    # Remove covered elements
    uncovered -= sets[best_set]

    # Remove selected set
    del sets[best_set]

print("Selected sets:", selected)
print("All elements are covered.")




# Subset Sum using Greedy Approximation

numbers = [3, 5, 7, 10, 12]
target = 15

# Sort numbers from largest to smallest
numbers.sort(reverse=True)

subset = []
total = 0

for num in numbers:
    if total + num <= target:
        subset.append(num)
        total += num

print("Numbers:", numbers)
print("Target:", target)
print("Selected subset:", subset)
print("Subset sum:", total)



# Vertex Cover using Approximation Algorithm

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D")
]

cover = []

while edges:

    # Select the first edge
    u, v = edges[0]

    # Add both vertices to cover
    cover.append(u)
    cover.append(v)

    # Remove all edges connected to u or v
    edges = [
        edge for edge in edges
        if u not in edge and v not in edge
    ]

print("Vertex Cover:", cover)
print("Number of vertices:", len(cover))



