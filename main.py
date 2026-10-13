# Personal expense tracker
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
            
            if amount <= 0:
                print("Amount should be greater than 0")
                continue
            
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number")

def view_expences():
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        expences = list(reader)
        
    if len(expences) <= 1:
        print("no expences founded")
        return
    
    print("\n=== your expences ===")
    
    for expense in expences[1:]:
        date, category, amount, description = expense
        print(f"{date} | {category} | {amount} | {description}")
def show_total():
    total = 0
    
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        
        for expense in reader:
            amount = float(expense[2])
            total += amount
            
        print(f"\nTotal expense: {total:.2f}")    
            
def show_menu():
    while True:
        print("\n=== expense tracker ===")
        print("1. add an expense")
        print("2. view all expenses")
        print("3. show total expenses")
        print("4. exit")
        
        choice = input("choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expences()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid choice. please choose 1 or 2")
      
        

    
create_file()
show_menu()
