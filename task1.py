import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        while amount >= coin:
            result[coin] = result.get(coin, 0) + 1
            amount -= coin
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [{} for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                new_coin_count = coin_used[i - coin].copy()
                new_coin_count[coin] = new_coin_count.get(coin, 0) + 1
                coin_used[i] = new_coin_count
    return coin_used[amount]

if __name__ == "__main__":
    amount_to_change = 113

    print(f"Amount to change: {amount_to_change}")

    # Greedy Algorithm Performance
    start_time = time.time()
    greedy_result = find_coins_greedy(amount_to_change)
    end_time = time.time()
    print(f"\nGreedy Algorithm Result: {greedy_result}")
    print(f"Greedy Algorithm Time: {end_time - start_time:.6f} seconds")

    # Dynamic Programming Algorithm Performance
    start_time = time.time()
    dp_result = find_min_coins(amount_to_change)
    end_time = time.time()
    print(f"\nDynamic Programming Algorithm Result: {dp_result}")
    print(f"Dynamic Programming Algorithm Time: {end_time - start_time:.6f} seconds")

    print("\n--- Testing with a larger amount (e.g., 1000) ---")
    amount_to_change_large = 1000

    print(f"Amount to change: {amount_to_change_large}")

    # Greedy Algorithm Performance (Large Amount)
    start_time = time.time()
    greedy_result_large = find_coins_greedy(amount_to_change_large)
    end_time = time.time()
    print(f"\nGreedy Algorithm Result (Large): {greedy_result_large}")
    print(f"Greedy Algorithm Time (Large): {end_time - start_time:.6f} seconds")

    # Dynamic Programming Algorithm Performance (Large Amount)
    start_time = time.time()
    dp_result_large = find_min_coins(amount_to_change_large)
    end_time = time.time()
    print(f"\nDynamic Programming Algorithm Result (Large): {dp_result_large}")
    print(f"Dynamic Programming Algorithm Time (Large): {end_time - start_time:.6f} seconds")
