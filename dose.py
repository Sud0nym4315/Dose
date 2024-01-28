#!/bin/python3
import os
import sys
import csv
import time
import pandas as pd

# Global vars
operation_mode = ".base/mode"
user_status = ".base/new_user"
db_path_ref = ".base/database_name"
chemical_database = ".base/drugs"

def clear():
    os.system("clear")

def err():
    clear()
    print("Something went wrong")
    sys.exit(1)

def create_db():
    db_new = "database.csv"

    # Create log db
    with open(db_new, "w", newline="") as f:
        db = csv.writer(f)
        db.writerow(["Chemical", "Dose", "Timestamp", "Hash check"])

    # Create drug database
    with open(".base/drugs", "w", newline='') as drugslist:
        drugs = csv.writer(drugslist)
        drugs.writerow(["Chemical name", "Brand name", "Classification"])

    # Add db name to file for future program reference
    with open(db_path_ref, "w") as f:
        f.write(db_new)

    # Change new user status
    with open(user_status, "w") as f:
        f.write("1")
    
    clear()
    print("Database successfully created!\n\n")
    time.sleep(3)
    clear()

def import_db():
    clear()
    db_imported = input("Enter full database path: ")
    check = os.path.isfile(db_imported)
    if check == True:
        with open(db_path_ref, "w") as f:
            f.write(db_imported)

def check_userstat():
    new_user = int(open(user_status, "r").read())
    if new_user == 0:
        print("It looks like this is your first time using this program.\nWould you like to create a new database or import one?\n\n")
        print("1) Create")
        print("2) Import")
        print("3) Exit\n")
        x = int(input("Choice: "))
        if x == 1:
            create_db()
        elif x == 2:
            import_db()
        else:
            print("Invalid option.")

    elif new_user != 1:
        err()


# Primarily to maintain the integrity of the data
# When not using the app. Key needs to either be
# stored in dir with proper perms or offloaded to
# a server to work
#def encrypt_db():

# Load base variables
check_userstat()

# load operation mode
# TODO: error handling
mode = open(operation_mode, "r").read()

# Read from stored db reference
with open(db_path_ref, "r") as f:
    db_path = f.read()

clear()    
# =================

with open(".base/banner", "r") as banner:
    x = banner.read()
    print(x)

with open(".base/menu", "r") as menu:
    count = 0
    for line in menu:
        if line != "\n": # avoid numbering blank lines
            count += 1
            print(str(count)+") "+line.rstrip())
        elif line == "\n": # still keep formatting
            print(line.strip())
    print("\n")


choice = int(input("Choice: "))
if choice == 1:
    print("1")
    # ask drug
    # ask dose
    # capture timestamp
    # update db
elif choice == 2:
    clear()
    data = pd.read_csv(db_path)
    print(data)
elif choice == 3:
    clear()
    # Implement some form of authentication?


    chem = input("Chemical name: ")
    brand = input("Brand name: ")
    chemclass = input("Classification: ")

    with open(".base/drugs", "a", newline='') as drugslist:
        drugs = csv.writer(drugslist)
    
        # ask input
        drugs.writerow([chem, brand, chemclass])





# close db


