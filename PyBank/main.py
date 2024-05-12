# import the required libraries

import os
import csv

# declare and instatiate the variables
total_pl = 0
total_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

# set path to the budget data and the output file
cwd = os.path.abspath(__file__)
dir_name = os.path.dirname(cwd)
datapath = os.path.join(dir_name, 'Resources', 'budget_data.csv')
outpath = os.path.join(dir_name, "analysis", "Financial_Analysis.txt")


# open the data file

with open(datapath) as csvfile:

    ## use csv reader to read data from the file
    reader = csv.reader(csvfile)
    data = list(reader)

    # remove the header
    data = data[1:]

# convert the 'Profit/Losses' column to integers
    profits_losses = [int(row[1]) for row in data]

# **********************************************************************************
#                           find total number of months
# **********************************************************************************
    total_months = len(data)


# **********************************************************************************
#                           calculate the total
# **********************************************************************************

total_pl = sum(profits_losses)

# **********************************************************************************
#                   find Average Change
# **********************************************************************************

# Iterate over the profits/losses
for i in range(1, len(profits_losses)):

    # Calculate the change from the previous month
    change = profits_losses[i] - profits_losses[i - 1]
    
    # Add the change to the total change
    total_change += change

# Calculate the average change and round off to precision 2
average_change = round(total_change / (len(profits_losses) - 1),2)


# **********************************************************************************
#                   get Greatest Increase
# **********************************************************************************

# iterate over the profits/losses
for i in range(1, len(profits_losses)):

    # calculate the increase from the previous month
    increase = profits_losses[i] - profits_losses[i - 1]
    
    # if this increase is greater than the current greatest increase, update the greatest increase and the month
    if increase > greatest_increase:
        greatest_increase = increase
        greatest_increase_month = data[i][0]

# **********************************************************************************
#                   get Greatest Decrease
# **********************************************************************************

# iterate over the profits/losses
for i in range(1, len(profits_losses)):

    # calculate the decrease from the previous month
    decrease = profits_losses[i - 1] - profits_losses[i]
    
    # if this decrease is greater than the current greatest decrease, update the greatest decrease and the month
    if decrease > greatest_decrease:
        greatest_decrease = decrease
        greatest_decrease_month = data[i][0]


# **********************************************************************************
#                   Output results to text file
# **********************************************************************************
# Open the output file
with open(outpath, 'w') as f:
    # Write the output to the file
    f.write(f"Financial Analysis\n")
    f.write(f"---------------------------------------\n")
    f.write(f"Total Months: {total_months}.\n")
    f.write(f"Total: ${total_pl}.\n")
    f.write(f"Average Change: {average_change}.\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}).\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_month} ($-{greatest_decrease}).\n")
