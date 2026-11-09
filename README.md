# Shop Inventory

A command-line inventory and sales tracker for a small food shop, written in Python.

## Features
- Add a new product with its price and stock
- Record a sale and reduce the stock automatically
- View all stock
- Low stock report (products with 4 or fewer left)
- See today's total sales
- End-of-day message based on total sales when you quit

## How to run
1. Install Python 3.
2. Download `shop_inventory.py`.
3. Run it: `python shop_inventory.py`
4. Enter your name, then choose an option from the menu.

## Menu
1. Add a new product
2. Record a sale
3. View all stock
4. Low stock report
5. Today's total sales
6. Quit

## Input checks
- The menu rejects letters and numbers outside 1 to 6
- Product names must be letters only, and duplicates are rejected
- Price must be above zero, and stock cannot be negative
- A sale is blocked if the quantity is zero, negative or more than the stock

## What I practiced
Dictionaries, lists, functions, loops, list comprehensions and error handling with try/except.

## Known limits
Data is kept in memory only, so stock changes and sales reset when the program closes.

## Planned improvements
- Cleaner stock display, one product per line
- Save stock and sales to a file
