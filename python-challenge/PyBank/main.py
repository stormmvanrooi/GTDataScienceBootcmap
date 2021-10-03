import csv
import os

budget_data = os.path.join("/Users/svanrooi/DataViz/python_challenge/PyBank/Resources/budget_data.csv")

#set variables 
total_months = 0
net_profit =0
changes =[]
month_count = []
gi = 0
gim = 0
gd = 0
gdm = 0

# Open the CSV
with open(budget_data, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

# The total number of months included in the dataset & net total
    previous_row = int(row[1])
    total_months = total_months + 1
    net_profit = net_profit + int(row[1])
    gi = int(row[1])
    gim = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        net_profit = net_profit + int(row[1])

        # Calculate change from month to month
        change = int(row[1]) - previous_row
        changes.append(change)
        previous_row = int(row[1])
        month_count.append(row[0])

    # Calculate average
    average_change = sum(changes)/len(changes)   
    
    #calculating the greatest increase
    if int(row[1]) > gi:
        gi = int(row[1])
        gim = row[0]
           
    #calculating the greatest decrease
    if int(row[1]) < gd:
        gd = int(row[1])
        gdm = row[0]

    # printing all values
print("Financial Analysis")
print("_________________________________")
print("Total Months: " + str(total_months))
print("Total Amount: $" + str(net_profit))
print("Average Change: $",average_change)
print("Greatest Increase:", gim, "$",max(changes))
print("Greatest Decrease:", gdm, "$",min(changes))

#write text file
output_file = os.path.join("/Users/svanrooi/DataViz/python_challenge/PyBank/Resources/financial_analyst.txt")

with open(output_file, 'w',) as txt:

    txt.write("Financial Analysis\n")
    txt.write("_________________________________\n")
    txt.write(f"Total Months: + ${total_months} \n")
    txt.write(f"Total Amount: $ + ${net_profit}\n")
    txt.write(f"Average Change: $,{average_change} \n")
    txt.write(f"Greatest Increase:, {gim} ${max(changes)}\n")
    txt.write(f"Greatest Decrease:, {gdm} ${min(changes)}\n")
