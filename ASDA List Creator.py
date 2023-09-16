import pandas as pd

# Take a series of items to buy entered by user and convert to data frame
user_input = input("Enter a list of items separated by spaces: ")
user_list = user_input.split()
shopping_list = pd.DataFrame(user_list, columns=['item'])

# Create a dictionary of items and their locations in ASDA
import csv
itm_loc_reader = csv.reader(open('C:/Users/seans/Desktop/ASDA List Creator/item_locations.csv'))
item_loc_dict = {}
for row in itm_loc_reader:
    key = row[1]
    item_loc_dict[key] = row[0]

# Add locations to the shopping list dataframe
user_list_locs = shopping_list.replace({"item": item_loc_dict})
shopping_list["location"] = user_list_locs["item"]

# Order shopping list by location and print the shopping list items 
shopping_list = shopping_list.sort_values(by=["location"])
print(shopping_list["item"])
