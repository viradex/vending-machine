# Item prices are in dollars
items = {
	"A": 1.2,
	"B": 0.6,
	"C": 0.75,
}

# Coins are in cents to avoid floating-point imprecision
coins = [200, 100, 50, 20, 10, 5]

print("Available items:")
for item in items:
	print(f"{item}: ${items[item]:.2f}")

# Ask for purchase letter and check if it exists
item = input("\nWhat item would you like to buy? ").upper()
if item not in items.keys():
	print(f"Item {item} does not exist!")
	exit(1)

# Get price of item
price = items[item]
print(f"Item {item} costs ${price:.2f}!\n")

# Get payment from user, with validation check
try:
	pay = float(input("How much do you want to pay? "))
except ValueError:
	print("The value is not a number!")
	exit(1)

# Check if payment is too low
if price > pay:
	print(f"You didn't pay enough! Item {item} costs ${price:.2f}, but you only paid ${pay:.2f}")
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

if not len(change):
    print("Thanks for paying the exact price!")
else:
	print("Thanks for paying! Here's your change:")

    # Print change in dollars
	for coin in coins:
		count = change.count(coin)
		if count > 0:
			print(f"{count} x ${coin/100:.2f}")
