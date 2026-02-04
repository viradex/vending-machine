from random import randint

items = {
	"A": 120,
	"B": 60,
	"C": 75,
}

# In form: { value: stock }
min_value = 5
max_value = 15
coins = {
	200: randint(min_value, max_value),
	100: randint(min_value, max_value),
	50: randint(min_value, max_value),
	20: randint(min_value, max_value),
	10: randint(min_value, max_value),
	5: randint(min_value, max_value)
}

print("Available items:")
for item in items:
	print(f"{item}: ${items[item] / 100:.2f}")

while True:
	item = input("\nWhat item would you like to buy? ").upper()
	if item in items.keys():
		break
	elif not item:
		exit(0)
	else:
		print(f"The item {item} does not exist!")
		continue

price = items[item]
print(f"Item {item} costs ${price / 100:.2f}!\n")

print("Accepted coins:")
for coin in coins.keys():
	if coin >= 100:
		print(f"{coin}¢ (${int(coin/100)})")
	else:
		print(f"{coin}¢")

total_paid = 0
while True:
	pay_input = input("\nWhat coin would you like to desposit (in cents)? ")

	if not pay_input:
		print("Exiting...")
		exit(0)

	try:
		pay = int(pay_input)
	except ValueError:
		print("The value entered is not a number!")
		continue

	if pay not in coins.keys():
		print(f"The {pay}¢ coin is not accepted, sorry!")
		continue
	
	total_paid += pay
	coins[pay] += 1

	if total_paid >= price:
		print(f"Thanks, you paid for item {item} for ${total_paid/100:.2f}!")
		break

	print(f"Amount paid so far: ${total_paid/100:.2f} / ${price:.2f}")

change = []
change_due = total_paid - price

if not len(change):
	print(f"Receiving change: ${change_due/100:.2f}")

print()

for coin in coins.keys():
	while change_due >= coin and coins[coin] > 0:
		change_due -= coin
		coins[coin] -= 1

		change.append(coin)

if change_due > 0:
	print(f"Sorry, we were not able to give you exact change. Please accept this refund of ${total_paid/100:.2f}.")
if not len(change):
    print("Thanks for paying the exact price!")
else:
	print("Thanks for paying! Here's your change:")

	for coin in coins.keys():
		count = change.count(coin)
		if count > 0:
			print(f"{count} x ${coin/100:.2f}")
