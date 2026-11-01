#huffman coding
import heapq
import math

def huffman(frequencies):

    # Create a priority queue
    heap = [(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build Huffman Tree
    while len(heap) > 1:
        f1, left = heapq.heappop(heap)
        f2, right = heapq.heappop(heap)

        new_node = {'0': left, '1': right}

        heapq.heappush(heap, (f1 + f2, new_node))

    # Generate Huffman Codes
    codes = {}

    def generate(node, code):
        if isinstance(node, str):
            codes[node] = code
        else:
            generate(node['0'], code + '0')
            generate(node['1'], code + '1')

    generate(heap[0][1], "")

    # Calculate bits
    huff_bits = sum(frequencies[ch] * len(codes[ch]) for ch in codes)

    total = sum(frequencies.values())
    fixed_bits = total * math.ceil(math.log2(len(frequencies)))

    saved_bits = fixed_bits - huff_bits

    # Display results
    print("Huffman Codes:", codes)
    print("Total Huffman Bits:", huff_bits)
    print("Fixed Bits:", fixed_bits)
    print("Bits Saved:", saved_bits)


# Main program
freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}

huffman(freq)
#Activity Selection Code
def activity_selection(start, finish):

    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]
    last_finish = activities[0][1]

    # Select activities
    for s, f in activities[1:]:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    # Display selected activities
    print("Selected Activities:")

    for i, (s, f) in enumerate(selected, 1):
        print("Activity", i, "Start:", s, "Finish:", f)

    print("Total Activities:", len(selected))


# Main program
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

activity_selection(start, finish)
