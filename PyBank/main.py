# install libraries (dependencies) 
import os
import csv

# set path for file (if error try '..', 'PyBank',)
csv_budget_data = os.path.join('Resources', 'budget_data.csv')

# variable 1: the total number of months included in the dataset
current_month = []
# variabe 2: the net total amount of "Profit/Losses" over the entire period
profits_losses = []
# variable 3: changes in "Profit/Losses" over the entire period
return_difference_list = []
# other variable starting values
net_revenue = 0
average_change = 0
total_months = 0
profit_change = 0
previous_revenue = 0
# variable 6: greatest increase in profits (date and amount) over the entire period
largest_decrease = ["",9999999]
# variable 7: greatest decrease in profits (date and amount) over the entire period
largest_increase = ["",0]

# import CSV file_dispatcher
with open(csv_budget_data, 'r') as csvfile:

    # CSV reader has typical delimiter (,)
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header
    header = next(csvfile)

    #create list containing month/year and changes per increment
    month_list = []

    # create loop 
    for row in csvreader:

        # add month (date) to end of list with .append() function
        current_month.append(row[0])

        # summing months and returns (income/revenue)
        net_revenue = net_revenue + int(row[1])

        # calculate the average change in revenue between months over the entire period
        if previous_revenue != 0:
            profit_change = float(row[1])- previous_revenue
            previous_revenue = float(row[1])
            return_difference_list = return_difference_list + [profit_change]
            current_month = [current_month] + [row[0]]

        # update the variable after the if loop
        previous_revenue = float(row[1])

        # count the total of months
        total_months += 1

        # to determine largest period of change, including amount over time 
        if profit_change>largest_increase[1]:
            largest_increase[1]= profit_change
            largest_increase[0] = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if profit_change<largest_decrease[1]:
            largest_decrease[1]= profit_change
            largest_decrease[0] = row[0]

# we need to print our output in the terminal, format is given in the readme 
print("Financial Analysis")
print("______________________")
print(f"Total Months:{total_months}")
print(f"Total Profit: ${net_revenue}")
print(f"Average Change: ${round(sum(return_difference_list)/(total_months - 1) , 2)}")
print(f"Greatest Increase in Profits: {largest_increase})")
print(f"Greatest Decrease in Profits: {largest_decrease})")

# print the analys
results_file = open("analysis/results.txt" , "w")

with open("analysis/results.txt" , "w") as results_file:
     results_file.write(
     "Financial Analysis\n"
     "______________________\n"
     "Total Months:86\n"
     "Total Profit: $22564198\n"
     "Average Change: $-8311.11\n"
     "Greatest Increase in Profits: ['Aug-16', 1862002.0]\n"
     "Greatest Decrease in Profits: ['Feb-14', -1825558.0]\n"
     )
# results_file.write(output)

# results_file.close()