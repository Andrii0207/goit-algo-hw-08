import heapq


def merge_k_lists(arr):

    flattened_arr = [item for sublist in arr for item in sublist]

    heap = []

    for value in flattened_arr:
        heapq.heappush(heap, value)

    return [heapq.heappop(heap) for _ in range(len(heap))]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)  # [1, 1, 2, 3, 4, 4, 5, 6]
