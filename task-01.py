import heapq


def optimal_expenses(iterable):

    total_cost = 0

    heapq.heapify(iterable)
    print("Початкова купа:", iterable)

    while len(iterable) > 1:

        first = heapq.heappop(iterable)
        second = heapq.heappop(iterable)
        cost = first + second
        total_cost += cost

        heapq.heappush(iterable, cost)

        print(f"З'єднали {first} і {second}, отримали {cost}")
        print("Оновлена купа:", iterable)
        print("Поточні загальні витрати:", total_cost)
        print("-" * 30)

    return total_cost


arr = [7, 4, 1, 5, 10, 3]

result = optimal_expenses(arr)
print("result: ", result)

# --------------------
# sorted
# arr = [1, 4, 3, 5, 10, 7]

# 1 + 3 = 4 (4) [4, 4, 7, 10, 5]
# 4 + 4 = 8 (4 + 8 = 12) [5, 8, 7, 10]
# 5 + 7 = 12 (12 + 12 = 24) [8, 10, 12]
# 8 + 10 = 18 (24 + 18 = 42 ) [12, 18]
# 12 + 18 = 30 (42 + 30 = 72) [30]

# 4 + 8 + 12 + 18 + 30 = 72 ✅

# --------------------

# 1 + 3 = 4  [4, 4, 5, 7, 10]
# 4 + 4 = 8   [8, 5, 7, 10]
# 8 + 5 = 13  [13, 7, 10]
# 13 + 7 = 20  [20, 10]
# 20 + 10 = 30 [30]

# 4 + 8 + 13 + 20 + 30 = 75 ❌

# --------------------

# arr = [1, 4, 3, 5, 10, 7]

# 1 + 4 = 5 (5)
# 5 + 3 = 8 (8)
# 8 + 5 = 13 (13)
# 13 + 10 = 23 (23)
# 23 + 7 = 30 (30)

# 5 + 8 + 13 + 23 + 30 = 79 ❌

# --------------------

# arr = [7, 4, 1, 5, 10, 3]

# 7 + 4 = 11 (11)
# 11 + 1 = 12 (12)
# 12 + 5 = 17 (17)
# 17 + 10 = 27 (27)
# 27 + 3 = 30 (30)

# 11 + 12 + 17 + 27 + 30 = 97 ❌
