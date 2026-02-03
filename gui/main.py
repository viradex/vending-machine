# My hate for Tkinter has grown to a raging fire that burns with
# the fierce passion of a million suns.
import tkinter as tk

items = {
  "A": 1.2,
  "B": 0.6,
  "C": 0.75,
  "D": 2.5,
  "E": 3.25
}

root = tk.Tk()
root.title("Vending Machine")
root.geometry("800x700")

# Headings
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

# Buttons frame aligned to the right
buttons_frame_outer = tk.Frame(root)
buttons_frame_outer.pack(fill="x", padx=20, pady=20)

buttons_frame = tk.Frame(buttons_frame_outer)
buttons_frame.pack(side="right")  # this pushes buttons to the right

def buy_item(item, price):
  print(f"You bought {item} for ${price:.2f}")

for item, price in items.items():
  text = f"{item}: ${price:.2f}"
  btn = tk.Button(
    buttons_frame,
    text=text,
    font=("Arial", 16),
    width=15,
    command=lambda i=item, p=price: buy_item(i, p)
  )
  btn.pack(pady=5)

# Bottom-right image
photo = tk.PhotoImage(file="gui/machine.png")
img_label = tk.Label(root, image=photo)
img_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

root.mainloop()