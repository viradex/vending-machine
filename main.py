items = {
  "A": 1.2,
  "B": 0.6,
  "C": 0.75,
}
coins = [200, 100, 50, 20, 10, 5]

purchase_ltr = input("What item would you like to buy? ").upper()
if purchase_ltr not in items.keys():
  print(f"Item {purchase_ltr} does not exist!")
  exit(1)

price = items[purchase_ltr]

print(f"Item {purchase_ltr} costs ${price:.2f}!\n")

try:
  pay = float(input("How much do you want to pay? "))
except ValueError:
  print("The value is not a number!")
  exit(1)

if price > pay:
  print(f"You didn't pay enough! Item {purchase_ltr} costs ${price:.2f}, but you only paid ${pay:.2f}")
  exit(1)

print(f"You paid ${pay:.2f}!\n")

change = []
change_due = (pay - price) * 100
for coin in coins:
  while change_due >= coin:
    change_due = change_due - coin
    change.append(coin)

print("Thanks for paying! Here's your change:")

if not len(change):
  print("<no change>")
else:
  for c in change:
    print(f"${c/100:.2f}")
