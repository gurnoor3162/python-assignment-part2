menu = {
  "Paneer Tikka": {"category": "Starters", "price": 180.0, "available": True},
  "Chicken Wings": {"category": "Starters", "price": 220.0, "available": False},
  "Veg Soup": {"category": "Starters", "price": 120.0, "available": True},
  "Butter Chicken": {"category": "Mains", "price": 320.0, "available": True},
  "Dal Tadka": {"category": "Mains", "price": 180.0, "available": True},
  "Veg Biryani": {"category": "Mains", "price": 250.0, "available": True},
  "Garlic Naan": {"category": "Mains", "price": 40.0, "available": True},
  "Gulab Jamun": {"category": "Desserts", "price": 90.0, "available": True},
  "Rasgulla": {"category": "Desserts", "price": 80.0, "available": True},
  "Ice Cream": {"category": "Desserts", "price": 110.0, "available": False},
}

inventory = {
  "Paneer Tikka": {"stock": 10, "reorder_level": 3},
  "Chicken Wings": {"stock": 8, "reorder_level": 2},
  "Veg Soup": {"stock": 15, "reorder_level": 5},
  "Butter Chicken": {"stock": 12, "reorder_level": 4},
  "Dal Tadka": {"stock": 20, "reorder_level": 5},
  "Veg Biryani": {"stock": 6, "reorder_level": 3},
  "Garlic Naan": {"stock": 30, "reorder_level": 10},
  "Gulab Jamun": {"stock": 5, "reorder_level": 2},
  "Rasgulla": {"stock": 4, "reorder_level": 3},
  "Ice Cream": {"stock": 7, "reorder_level": 4},
}

sales_log = {
  "2025-01-01": [
    {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220},
    {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210},
    {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360},
  ],
  "2025-01-02": [
    {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220},
    {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340},
  ],
}

#task1
categories = ["Starters", "Mains", "Desserts"]

for cat in categories:
  print("====", cat, "====")
  for item in menu:
    if menu[item]["category"] == cat:
      status = "Available" if menu[item]["available"] else "Unavailable"
      print(item, "-", menu[item]["price"], "-", status)

print("Total items:", len(menu))

available_count = 0
for item in menu:
  if menu[item]["available"]:
    available_count += 1
print("Available items:", available_count)

max_item = None
max_price = 0
for item in menu:
  if menu[item]["price"] > max_price:
    max_price = menu[item]["price"]
    max_item = item
print("Most expensive:", max_item, max_price)

print("Items under 150:")
for item in menu:
  if menu[item]["price"] < 150:
    print(item, menu[item]["price"])


#task2
cart = []

def add_item(name, qty):
  if name not in menu:
    print("Item not found")
    return

  if not menu[name]["available"]:
    print("Item unavailable")
    return

  for c in cart:
    if c["item"] == name:
      c["quantity"] += qty
      return

  cart.append({"item": name, "quantity": qty, "price": menu[name]["price"]})


def remove_item(name):
  for c in cart:
    if c["item"] == name:
      cart.remove(c)
      return
  print("Item not in cart")


add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)
add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)
remove_item("Gulab Jamun")

print("Cart:", cart)

subtotal = 0
for c in cart:
  item_total = c["quantity"] * c["price"]
  subtotal += item_total
  print(c["item"], "x", c["quantity"], "=", item_total)

gst = subtotal * 0.05
total = subtotal + gst

print("Subtotal:", subtotal)
print("GST:", round(gst, 2))
print("Total:", round(total, 2))


#task3
import copy

inventory_backup = copy.deepcopy(inventory)

inventory["Paneer Tikka"]["stock"] = 2
print("Inventory:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

inventory = copy.deepcopy(inventory_backup)

#deducting stock
for c in cart:
  name = c["item"]
  qty = c["quantity"]

  if inventory[name]["stock"] >= qty:
    inventory[name]["stock"] -= qty
  else:
    print("Low stock for", name)
    inventory[name]["stock"] = 0

#alert for reorder
for item in inventory:
  if inventory[item]["stock"] <= inventory[item]["reorder_level"]:
    print("Reorder Alert:", item, inventory[item]["stock"])


#task4
#revenue per day
for day in sales_log:
  total = 0
  for order in sales_log[day]:
    total += order["total"]
  print(day, total)

#finding best day
best_day = None
best_total = 0

for day in sales_log:
  total = sum([o["total"] for o in sales_log[day]])
  if total > best_total:
    best_total = total
    best_day = day

print("Best day:", best_day)

#counting most ordered item
count = {}

for day in sales_log:
  for order in sales_log[day]:
    for item in order["items"]:
      if item not in count:
        count[item] = 0
      count[item] += 1

top_item = max(count, key=count.get)
print("Most ordered item:", top_item)

#adding a new day
sales_log["2025-01-05"] = [
  {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490},
  {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260},
]

#printing all orders
num = 1
for day in sales_log:
  for order in sales_log[day]:
    print(num, day, order["items"], order["total"])
    num += 1
