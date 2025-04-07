# def knapsack(weights, values, capacity):
#     n = len(weights)
#     # Initialize the DP table with zeros
#     B = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

#     # Build the table in bottom-up manner
#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i - 1] <= w:
#                 B[i][w] = max(values[i - 1] + B[i - 1][w - weights[i - 1]], B[i - 1][w])
#             else:
#                 B[i][w] = B[i - 1][w]

#     # Print the DP table
#     print("DP Table:")
#     for row in B:
#         print(row)

#     # The maximum value that can be obtained
#     return B[n][capacity]

# # Example usage:
# weights = [2, 3, 4, 5]
# values = [3, 4, 5, 6]
# capacity = 5
# max_value = knapsack(weights, values, capacity)
# print(f"Maximum value in knapsack: {max_value}")


import sys

def coin_change(N, Amt, C):
    # Base Case: If amount is 0, we need 0 coins
    if Amt == 0:
        return 0
    # If no coins left and amount > 0 → not possible
    if N == 0:
        return sys.maxsize  # acts like "infinity"

    if C[N-1] > Amt:
        return coin_change(N-1, Amt, C)
    else:
        return min(
            coin_change(N-1, Amt, C),                       # don't take current coin
            1 + coin_change(N-1, Amt - C[N-1], C)           # take current coin
        )

# Example usage:
coins = [1, 2, 3]     # Coin denominations
amount = 4
N = len(coins)

result = coin_change(N, amount, coins)

if result == sys.maxsize:
    print("Not possible to make the amount with given coins.")
else:
    print("Minimum coins required:", result)
