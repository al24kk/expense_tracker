import csv
import os
from datetime import datetime

FILE_NAME = "expence.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])
            
def add_expense():
    category = input("Enter the category: ")
    amount = get_amount()
    description = input("Enter the description: ")
    
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer= csv.writer(file)
        writer.writerow([date, category, amount, description])
        
def get_amount():
    while True:
        try:
            amount = float(input("Enter the price: "))
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number")
        

    
create_file()
add_expense()