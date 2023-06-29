import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_profit_losses = 0
    total_months = 0 
    sum_profit_losses = 0 

    for row in csvreader:
        
        profit_losses = int(row[1])
        #print(profit_losses)

        total_profit_losses = total_profit_losses + profit_losses
        total_months = total_months + 1
        
        if total_months > 1:
            change = profit_losses - last_profit_losses
            sum_profit_losses = sum_profit_losses + change

        last_profit_losses = int(row[1])
       

    average_change = (sum_profit_losses / (total_months -1))
    #print(total_profit_losses)
    #print(total_months)
    #print (average_change)

    # print output
    print('Financial Anlaysis')
    print('----------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit_losses}')
    print(f'Average Change: ${average_change}')
    print('Greatest increase in profits: ')
    print('Greatest decrease in profits: ')
