import time

# Функція жадібного алгоритму
def find_coins_greedy(amount):
    start_time = time.time()
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Функція динамічного програмування
def find_min_coins(amount):
    start_time = time.time()
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin

    result = {}
    x = amount
    while x > 0:
        coin = coin_used[x]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        x -= coin

    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Виводимо результати розрахунків загальної кількості монеток
amount = 113
greedy_result, greedy_time = find_coins_greedy(amount)
dp_result, dp_time = find_min_coins(amount)

print(f"Результат жадібного алгоритму: {greedy_result}, Time: {greedy_time}")
print(f"Результат функції динамічного програмівання: {dp_result}, Time: {dp_time}")

# Порівнюємо часові значення обох алгоритмів
if find_coins_greedy(amount) > find_min_coins(amount):
    print ("Функція динамічного програмування швидша")
else:
    print ("Функція жадібного алгоритму щвидша")