# Import functions
import os
import csv

# Assign the csv file to a variable and open it
budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, newline="") as csvfile:
    # Read the file to a variable
    read_data = csv.reader(csvfile, delimiter=",")
    
    # Read/skip the header row
    csv_header = next(csvfile)
    
    # Assign variable that will be changed
    net_total = 0
    months = 0
    change_total = 0
    previous_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    # Read through file
    for row in read_data:
        # Increase month count each row
        months += 1
        
        # Calculating the total
        net_total += int(row[1])
        
        # Calculating the average change
        current_change = int(row[1])
        # This if statement is to ensure that there is no value stored to change_total on the first row
        if read_data.line_num == 1:
            previous_change = int(row[1])
        change_total += (current_change - previous_change)

        # Calculating the greatest increase and greatest decrease
        if current_change > previous_change:
            current_increase = (current_change - previous_change)
            if current_increase > greatest_increase:
                greatest_increase = current_increase
                gi_date = str(row[0])
        elif current_change < previous_change:
            current_decrease = (current_change - previous_change)
            if current_decrease < greatest_decrease:
                greatest_decrease = current_decrease
                gd_date = str(row[0])
        
        # Setting current row to previous_change for use in the next row
        previous_change = int(row[1])

    # Printing everything out
    print(f'Total months: {months}')
    print(f'Total: ${"{:,}".format(net_total)}')
    average_change = change_total / (months - 1)
    print(f'Average change: ${"{:,.2f}".format(average_change)}')
    print(f'Greatest profit increase: {gi_date} (${greatest_increase})')
    print(f'Greatest profit decrease: {gd_date} (${greatest_decrease})')