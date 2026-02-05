from random import randint

password = "1234"

actions = {
    "1": "Buy item",
    "2": "Check coin stock",
    "3": "Add coin stock",
    "4": "Shut down",
}

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


def print_actions():
    default = "buy"

    print("Available actions:")
    for action in actions:
        print(f"{action}: {actions[action]} {"(default)" if action == default else ""}")


def enter_password():
    while True:
        attempt = input("Enter password: ")
        if attempt != password:
            print("Incorrect password! Please try again.\n")
            continue

        return


def get_coin_stock():
    print("\nCoin stock:")
    for coin in coins:
        print(f"${coin/100:.2f}: {coins[coin]}")


def print_items():
    print("Available items:")
    for item in items:
        print(f"{item}: ${items[item] / 100:.2f}")


def print_currency(enter_coins=True, enter_notes=True):
    if not enter_coins and not enter_notes:
        raise ValueError("At least one of enter_coins or enter_notes must be True")

    if enter_coins and enter_notes:
        print("Accepted coins and notes:")
    elif enter_coins:
        print("Accepted coins:")
    elif enter_notes:
        print("Accepted notes:")

    if enter_notes:
        for note in sorted(notes, reverse=True):
            print(f"{note}¢ (${int(note/100)})")

    if enter_coins:
        for coin in sorted(coins.keys(), reverse=True):
            if coin >= 100:
                print(f"{coin}¢ (${int(coin/100)})")
            else:
                print(f"{coin}¢")


def add_coin_stock():
    print_currency(True, False)

    while True:
        print("\n(to exit, enter nothing)")
        refill_input = input("What coin would you like to refill (in cents)? ")

        if not refill_input:
            return

        try:
            refill = int(refill_input)
        except ValueError:
            print("The value entered is not a number!")
            continue

        if refill not in coins.keys():
            print(f"{refill}¢ is not accepted, sorry!")
            continue

        value_input = input(
            f"How many coins would you like to add to the already existing stock of {coins[refill]}? "
        )

        try:
            value = int(value_input)
        except ValueError:
            print("The value entered is not a number!")
            continue

        if value <= 0 or value > 50:
            print("Value is out of range! Must be between 1-50.")
            continue

        coins[refill] += value
        print(f"New stock of ${refill/100:.2f}: {coins[refill]}")


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
    print_actions()
    action = input("\nWhat action would you like to do? ").lower()

    if action == "2":
        get_coin_stock()
        print()

        continue
    elif action == "3":
        enter_password()
        add_coin_stock()
        print()

        continue
    elif action == "4":
        print("Shutting down...")
        break

    # For action == 'buy'
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
