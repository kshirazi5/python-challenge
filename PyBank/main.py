#Import modules os and csv

import os
import csv

#Set the path for CSV file in csvpath

csvpath = os.path.join("Resources","budget_data.csv")

#Create the lists to store data and initialize values

profit = []
monthlyChanges = []
date = []
 
count = 0
totalProfit = 0
totalchangeProfits = 0
initialProfit = 0

# Open CSV using csvpath as set path

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Execute
    for row in csvreader:    
      # Use count to count the number months 
      count = count + 1 

      # For collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      totalProfit = totalProfit + int(row[1])

      #Calculate the average change in profits from month to month. Then calulate the average change in profits
      finalProfit = int(row[1])
      monthlychangeProfits = finalProfit - initialProfit

      #Store these monthly changes in a list
      monthlyChanges.append(monthlychangeProfits)

      totalchangeProfits = totalchangeProfits + monthlychangeProfits
      initialProfit = finalProfit

      #Calculate average change in profits
      averagechangeProfits = (totalchangeProfits/count)
      
      #Find max and min change in profits and the corresponding dates these changes were obeserved
      grtstincreaseProfits = max(monthlyChanges)
      grtstdecreaseProfits = min(monthlyChanges)

      increase_date = date[monthlyChanges.index(grtstincreaseProfits)]
      decrease_date = date[monthlyChanges.index(grtstdecreaseProfits)]
      
#Print into Terminal

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(totalProfit))
    print("Average Change: " + "$" + str(int(averagechangeProfits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(grtstincreaseProfits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(grtstdecreaseProfits)+ ")")
    print("----------------------------------------------------------")

#Open into text file

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(totalProfit) +"\n")
    text.write("    Average Change: " + '$' + str(int(averagechangeProfits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(grtstincreaseProfits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(grtstdecreaseProfits) + ")\n")
    text.write("----------------------------------------------------------\n")