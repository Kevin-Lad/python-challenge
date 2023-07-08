import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    total_profit_losses = 0
    total_months = 0 
    sum_profit_losses = 0 
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 999999999999
    greatest_decrease_month = ""

    # This for loop is where all the calculations will be done
    for row in csvreader:
        
        profit_losses = int(row[1])

        total_profit_losses = total_profit_losses + profit_losses
        total_months = total_months + 1
        
        if total_months > 1:
            change = profit_losses - last_profit_losses
            sum_profit_losses = sum_profit_losses + change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if change < greatest_decrease:
                greatest_decrease = change 
                greatest_decrease_month = row[0]
        
        last_profit_losses = int(row[1])
       
    average_change = (sum_profit_losses / (total_months -1))
    avg_change = round(average_change, 2)
    
    # print output
    print('Financial Anlaysis')
    print('----------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit_losses}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest increase in profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})')

# write to a text file
with open(output_path, 'w') as f:
    f.write('Financial Anlaysis\n')
    f.write('-----------------------\n')
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: ${total_profit_losses}\n')
    f.write(f'Average Change: ${avg_change}\n')
    f.write(f'Greatest increase in profits: {greatest_increase_month} (${greatest_increase})\n')
    f.write(f'Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})\n')


   
