# Command-Line Inventory & Order Manager

A Python tool that manages shipment orders stored in a CSV file, through a simple menu.

## Features
- Loads existing orders from a CSV file into memory
- View all pending orders
- View all overweight orders (over 20 kg)
- Add a new order
- Mark an order as delivered
- Saves all changes back to the CSV file on exit

## How to run
python order_manager.py

## What I learned
- Reading and writing CSV files with the csv module
- Working with a list of dictionaries, not just a single dictionary
- DictReader and DictWriter for structured file data
- Updating a dictionary inside a list by matching on a key
- Debugging with print statements to inspect data mid-program
- Careful attention to indentation, since Python relies on it completely
