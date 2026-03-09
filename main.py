import os

class Intro:
    def intro(self):
        title = "Expense Tracker"
        print(title.center(60,"-"))

    def menu1(self):
        self.menu11 = """\nWelcome to Expense Tracker
        -- Choose option your want to add/remove/see the Expense
             1. Essentials
             2. Food
             3. Personal
             4. Education
             5. Investment
             6. Monthly Total
             7. Exit and Save
        -- Enter the option 1,2,3,4,5,6,7 \n """
        print(self.menu11)

    def menu2(self):
        self.menu22 = """\nChoose option your want to add/remove/see the Expense
             1. Add
             2. Remove
             3. See Total
        -- Enter the option 1,2,3 \n"""
        print(self.menu22)

    
class Expense_Tracker:
    def __init__(self):
        self.file = "Expense.txt"
        self.expenses = []
        self.load_from_file()
        

    def add(self,category):
        try:
            amount = int(input("Enter the Money :"))
            self.expenses.append((category,amount))
            print("Expense Added Successfully ✅")
        except ValueError:
            print("oops you enter invalid value")
            print("Please Enter the amount in Numbers")
    
    def load_from_file(self):
        if os.path.exists(self.file):
            with open(self.file,"r") as f:
                for line in f:
                    category ,amount =line.strip().split(",")
                    self.expenses.append((category,int(amount)))
    
    def save_to_file(self):
        with open (self.file, "w") as f:
            for category ,amount in self.expenses:
                f.write(f"{category},{amount}\n")
    
    def remove(self,category):
        found = False
        for expense in self.expenses:
            if expense[0] == category:
                self.expenses.remove(expense)
                print("Expense Removed ✅")
                found = True
                break
        if not found:
             print("No expense found in this category.")
    
    def category_total(self, category):
        total = 0
        for cat, amount in self.expenses:
            if cat == category:
                total += amount
        print(f"Total of {category}: {total}") 

    def monthly_total(self):
        total = 0
        for _,amount in self.expenses:
            total += amount
        print(f"Montly total : {total} ")  


x = Intro()
tracker = Expense_Tracker()
x.intro()
while True:
    x.menu1()
    try:
      choose =int(input("Enter the option :"))
      if choose == 1:
          category = "Essentials"
      elif choose == 2:
          category = "Food"
      elif choose == 3:
          category = "Personal"
      elif choose == 4:
          category = "Education"
      elif choose == 5:
          category = "Investment"
      elif choose == 6:
          print(tracker.expenses)
          tracker.monthly_total()
          continue
      elif choose == 7:
          tracker.save_to_file()
          print("Data Saved Successfully. Exiting...")
          break
      
      else:
          print("\noops you choose wrong option")
          print("please choose the option below")
          continue

    except ValueError:
        print("\noops you enter invalid value")
        print("Please Enter the Number like 1,2,3..etc")
        continue
    
    x.menu2()
    try:
        sub = input("\nEnter the option: ")

        if sub == "1":
            tracker.add(category)
        elif sub == "2":
            tracker.remove(category)
        elif sub == "3":
            tracker.category_total(category)
        else:
            print("\noops you choose wrong option")
            print("please choose the option below")
            continue


    except ValueError:
        print("\noops you enter invalid value")
        print("Please Enter the Number like 1,2,3..etc")
        continue       




    

        

