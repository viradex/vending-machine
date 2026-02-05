from random import randint

items = {
    "A": 120,
    "B": 60,
    "C": 75,
}

# In form: { value: stock }
min_value = 5
max_value = 10
coins = {
    200: randint(min_value, max_value),
    100: randint(min_value, max_value),
    50: randint(min_value, max_value),
    20: randint(min_value, max_value),
    10: randint(min_value, max_value),
    5: randint(min_value, max_value),
}

notes = [500, 1000, 2000]


def print_items():
    print("Available items:")
    for item in items:
        print(f"{item}: ${items[item] / 100:.2f}")


def print_currency():
    print("Accepted coins and notes:")
    for note in sorted(notes, reverse=True):
        print(f"{note}¢ (${int(note/100)})")

    for coin in sorted(coins.keys(), reverse=True):
        if coin >= 100:
            print(f"{coin}¢ (${int(coin/100)})")
        else:
            print(f"{coin}¢")


def select_item():
    while True:
        item = input("\nWhat item would you like to buy? ").upper()
        if item in items.keys():
            return item
        elif not item:
            return None
        else:
            print(f"The item {item} does not exist!")
            continue


def get_money_deposited(price):
    total_paid = 0
    while True:
        pay_input = input("\nWhat coin/note would you like to deposit (in cents)? ")

        if not pay_input:
            return None

        try:
            pay = int(pay_input)
        except ValueError:
            print("The value entered is not a number!")
            continue

        if pay not in coins.keys() and pay not in notes:
            print(f"{pay}¢ is not accepted, sorry!")
            continue

        total_paid += pay
        if pay in coins.keys():
            coins[pay] += 1

        if total_paid >= price:
            print(f"Thanks! Total inserted: ${total_paid/100:.2f}!")
            return total_paid

        print(f"Amount paid so far: ${total_paid/100:.2f} / ${price/100:.2f}")


def calc_change(total_paid, price):
    change_due = total_paid - price
    temp_coins = coins.copy()
    temp_change = []
    temp_due = change_due

    if change_due > 0:
        print(f"Receiving change: ${change_due/100:.2f}")

    print()

    for coin in sorted(temp_coins.keys(), reverse=True):
        while temp_due >= coin and temp_coins[coin] > 0:
            temp_due -= coin
            temp_coins[coin] -= 1
            temp_change.append(coin)

    if temp_due > 0:
        return None, None

    return temp_coins, temp_change


def print_change(change):
    if not len(change):
        print("Thanks for paying the exact price!")
    else:
        print("Thanks for paying! Here's your change:")

        for coin in sorted(set(change), reverse=True):
            count = change.count(coin)
            if count > 0:
                print(f"{count} x ${coin/100:.2f}")


while True:
    print_items()

    item = select_item()
    if item is None:
        print("No item selected, ending process...\n")
        continue

    price = items[item]
    print(f"Item {item} costs ${price / 100:.2f}!\n")

    print_currency()

    total_paid = get_money_deposited(price)
    if total_paid is None:
        print("Payment cancelled.\n")
        continue

    coins, change = calc_change(total_paid, price)
    if coins is None:
        print(f"Sorry, we were not able to give exact change.")
        print(f"Refunding ${total_paid/100:.2f}...\n")
        continue

    print_change(change)
    print()
