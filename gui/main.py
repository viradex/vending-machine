# My hate for Tkinter has grown to a raging fire that burns with
# the fierce passion of a million suns.
import tkinter as tk
from tkinter import ttk
from random import randint

items = {
  "A": 1.2,
  "B": 0.6,
  "C": 0.75,
  "D": 2.5,
  "E": 3.25
}

coins = [1000, 500, 200, 100, 50, 20, 10, 5]

root = tk.Tk()
root.title("Vending Machine")
root.geometry("900x700")

# -------------------- HEADINGS --------------------
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=10)

heading = tk.Label(
  top_frame,
  text="Vending Machine",
  font=("Arial", 24, "bold"),
  anchor="w"
)
heading.pack(side="left")

product_heading = tk.Label(
  top_frame,
  text="Products",
  font=("Arial", 20, "bold"),
  anchor="e"
)
product_heading.pack(side="right", padx=70)

# -------------------- MAIN CONTENT --------------------
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

# LEFT COLUMN (Products)
left_frame = tk.Frame(content_frame)
left_frame.pack(side="left", anchor="n")

# separator = ttk.Separator(content_frame, orient="vertical")
# separator.pack(side="left", fill="y", padx=20)

right_frame = tk.Frame(content_frame)
right_frame.pack(side="right", anchor="n")

# -------------------- PRODUCTS --------------------
def buy_item(item, price):
  print(f"You bought {item} for ${price:.2f}")

buttons_frame = tk.Frame(right_frame)
buttons_frame.pack(anchor="n")

for item, price in items.items():
  btn = tk.Button(
    buttons_frame,
    text=f"{item}: ${price:.2f}",
    font=("Arial", 16),
    width=15,
    command=lambda i=item, p=price: buy_item(i, p)
  )
  btn.pack(pady=5)

# -------------------- COINS ROW WITH STACKS --------------------
coins_frame = tk.Frame(root)
coins_frame.pack(side="bottom", anchor="w", pady=20, padx=20)  # anchored left

def insert_coin(value):
  print(f"Inserted ${value / 100:.2f} ({value} cents)")

for coin in coins:
  # Create a column frame for this coin
  col_frame = tk.Frame(coins_frame)
  col_frame.pack(side="left", padx=5)

  # Coin button at the bottom
  coin_btn = tk.Button(
    col_frame,
    text=f"${coin / 100:.2f}",
    font=("Arial", 12),
    width=6,
    command=lambda v=coin: insert_coin(v)
  )
  coin_btn.pack(side="bottom", pady=5)

  # Stack of thin rectangles above the button
  for i in range(randint(1, 5)):  # random stack height
    rect = tk.Label(
      col_frame,
      bg="black",
      width=5,
      height=1
    )
    rect.pack(side="bottom", pady=1)  # pack above previous widgets


# -------------------- IMAGE --------------------
photo = tk.PhotoImage(file="machine.png")
img_label = tk.Label(root, image=photo)
img_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

root.mainloop()
