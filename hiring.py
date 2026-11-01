import math
import random

def hiring_problem(scores):
    n = len(scores)
    k = math.ceil(n / math.e)  # k = 37 for 100 candidates
    
    # 1. Observe phase: Find best score in first 37
    benchmark = max(scores[:k])
    print(f"Candidates observed: {k}")
    print(f"Benchmark score: {benchmark}")
    
    # 2. Select phase: Pick first candidate that beats benchmark
    for i in range(k, n):
        if scores[i] > benchmark:
            print(f"Selected Candidate {i + 1} (Score: {scores[i]})")
            return
            
    # Fallback: Pick last candidate
    print(f"Selected Candidate {n} (Score: {scores[-1]})")

# Generate 100 scores (or replace with your custom list)
scores = [random.randint(1, 100) for _ in range(100)]

hiring_problem(scores)