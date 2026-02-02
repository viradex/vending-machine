from random import randint

items = {
  "A": 1.2,
  "B": 0.6,
  "C": 0.75,
  "D": 2.5,
  "E": 3.25,
}

min_stock = 0
max_stock = 2
coins = [
  { "value": 1000, "stock": randint(min_stock, max_stock) },
  { "value": 500, "stock": randint(min_stock, max_stock) },
  { "value": 200, "stock": randint(min_stock, max_stock) },
  { "value": 100, "stock": randint(min_stock, max_stock) },
  { "value": 50, "stock": randint(min_stock, max_stock) },
  { "value": 20, "stock": randint(min_stock, max_stock) },
  { "value": 10, "stock": randint(min_stock, max_stock) },
  { "value": 5, "stock": randint(min_stock, max_stock) },
]

def get_change(payment):
  coins_used = []
  changes = []

  for coin in coins:
    while payment >= coin["value"] and coin["stock"] > 0:
      payment -= coin["value"]
      coins_used.append(coin["value"])

      coin["stock"] -= 1
      changes.append(coin)

  if payment != 0 :
    for coin in changes:
      coin["stock"] += 1
    return None
  
  return coins_used

def add_payment_to_stock(amount):
  for coin in coins:
    while amount >= coin["value"]:
      coin["stock"] += 1
      amount -= coin["value"]

print("VENDING MACHINE")

while True:
  print(f"\nAvailable items: {", ".join(items.keys())}")

  purchase_ltr = input("What item would you like to buy? (Q to quit) ").upper()

  if purchase_ltr == "Q":
    print("Thanks for using the vending machine!")
    break

  if purchase_ltr not in items.keys():
    print(f"Item {purchase_ltr} does not exist!")
    continue

  price = items[purchase_ltr]
  print(f"Item {purchase_ltr} costs ${price:.2f}!\n")

  try:
    pay = float(input("How much do you want to pay? "))
  except ValueError:
    print("The value is not a number!")
    continue

  if price > pay:
    print(f"You didn't pay enough! Item {purchase_ltr} costs ${price:.2f}, but you only paid ${pay:.2f}")
    continue

  change = get_change((pay - price) * 100)

  if change is None:
    print("Sorry, exact change not available.")
    continue

  print(f"You paid ${pay:.2f}!\n")
  add_payment_to_stock(pay * 100)
  print("Thanks for paying!")

  print("Here's your change:")
  for c in change:
    print(f"${c/100:.2f}")

  print("\nCoin stock:")
  for c in coins:
    print(f"${c['value']/100:.2f}: {c['stock']}")

