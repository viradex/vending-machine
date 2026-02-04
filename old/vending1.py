
# Item prices are in dollars
items = {
    "A": 1.2,
    "B": 0.6,
    "C": 0.75,
}

# Coins are in cents to avoid floating-point imprecision
coins = [200, 100, 50, 20, 10, 5]

# Ask for purchase letter and check if it exists
purchase_ltr = input("What item would you like to buy? ").upper()
if purchase_ltr not in items.keys():
    print(f"Item {purchase_ltr} does not exist!")
    exit(1)

# Get price of item
price = items[purchase_ltr]
print(f"Item {purchase_ltr} costs ${price:.2f}!\n")

# Get payment from user, with validation check
try:
    pay = float(input("How much do you want to pay? "))
except ValueError:
    print("The value is not a number!")
    exit(1)

# Check if payment is too low
if price > pay:
    print(f"You didn't pay enough! Item {purchase_ltr} costs ${price:.2f}, but you only paid ${pay:.2f}")
    exit(1)

print(f"You paid ${pay:.2f}!\n")

# Change, and change due (converted to cents)
change = []
change_due = (pay - price) * 100

# Go through all coins and only add to change if it's the highest that can
# be added without going below zero
for coin in coins:
    while change_due >= coin:
        change_due -= coin
        change.append(coin)

print("Thanks for paying! Here's your change:")

if not len(change):
    print("<no change>")
else:
    # Print change in dollars
    for c in change:
        print(f"${c/100:.2f}")
